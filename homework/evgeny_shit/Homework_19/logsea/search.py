from tkinter import messagebox
from typing import List, Tuple


def search_text_in_file(file_path: str, search_text: str, first_only: bool) -> List[Tuple[int, str]]:
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
                        context_words = words[start:end]
                        context_text = ' '.join(context_words)
                        results.append((line_number, context_text))
                        if first_only:
                            break
                    if first_only and results:
                        break
    except Exception as e:
        messagebox.showerror("Error", f"Error reading file {file_path}: {str(e)}")
    return results
