import os
import argparse

parser = argparse.ArgumentParser(description="text search")
parser.add_argument("folder_path", help="enter folder path")
parser.add_argument("--text", help="WARN", required=True)

args = parser.parse_args()

if os.path.exists(args.folder_path) and os.path.isdir(args.folder_path):
    for file_name in os.listdir(args.folder_path):
        file_path = os.path.join(args.folder_path, file_name)
        if os.path.isfile(file_path):
            with open(file_path, encoding='utf-8') as file:
                found = False
                for line_number, line in enumerate(file, start=1):
                    if args.text in line:
                        found = True
                        words = line.split()
                        indices = [i for i, word in enumerate(words) if args.text in word]
                        for word_index in indices:
                            start_index = max(0, word_index - 5)
                            end_index = min(len(words), word_index + 6)
                            context = ' '.join(words[start_index:end_index])
                            print(f"{line_number}: {context} в файле {file_path}")
                if not found:
                    print(f'Текст {args.text} не найден в файле {file_path}')
else:
    print(f"Папка {args.folder_path} не существует.")
