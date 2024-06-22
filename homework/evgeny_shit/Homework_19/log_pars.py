import os
import argparse
from typing import List, Tuple
from rich.table import Table
from rich.console import Console


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Search the log files')
    parser.add_argument('path', type=str, help='Path to the log files directory')
    parser.add_argument('--text', type=str, required=True, help='Text to search for in log files')
    parser.add_argument('--first', action='store_true', help='Show only the first occurrence in each file')
    return parser.parse_args()


def search_text_in_file(console: Console, file_path: str, search_text: str, first_only: bool) -> List[Tuple[int, str]]:
    results = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if search_text in line:
                    words = line.split()
                    indices = [i for i, word in enumerate(words) if search_text in word]
                    for index in indices:
                        start = max(index - 5, 0)
                        end = index + 6
                        context = ' '.join(words[start:end])
                        results.append((line_number, context))
                        if first_only:
                            break
                    if first_only and results:
                        break
    except Exception as e:
        console.print(f"Error reading file {file_path}: {e}", style="bold red")
    return results


def create_result_table() -> Table:
    table = Table()
    table.add_column("File", justify="center")
    table.add_column("Line", header_style="yellow", style="yellow", justify="center")
    table.add_column("Context", header_style="green", style="green", justify="center")
    return table


def display_results(console: Console, table: Table, found_anything: bool, search_text: str) -> None:
    if found_anything:
        console.print(table)
    else:
        console.print(f"No occurrences of '{search_text}' were found in the log files.", style="bold yellow")


def main() -> None:
    console = Console()
    args = parse_arguments()
    log_files_path = args.path
    search_text = args.text
    first_only = args.first

    if not os.path.isdir(log_files_path):
        console.print(f"The path {log_files_path} is not a valid directory.", style="bold red")
        return

    console.print(f"\nSearching for '{search_text}' in {log_files_path}", style="bold")

    table = create_result_table()
    found_anything = False

    for root, _, files in os.walk(log_files_path):
        for file in files:
            file_path = str(os.path.join(root, file))
            matches = search_text_in_file(console, file_path, search_text, first_only)
            for line_number, context in matches:
                table.add_row(file, str(line_number), context)
                found_anything = True

    display_results(console, table, found_anything, search_text)


if __name__ == '__main__':
    main()
