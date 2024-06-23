import os
import argparse


parser = argparse.ArgumentParser(description="text search")
parser.add_argument("file_path", help="enter file path")
parser.add_argument("--text", help="WARN", required=True)

args = parser.parse_args()

if os.path.exists(args.file_path) and os.path.isfile(args.file_path):
    with open(args.file_path, encoding='utf-8') as file:
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
                    print(f"{line_number}: {context} в файле {args.file_path}")
        if not found:
            print('Текст не найден в файле.')
else:
    print(f"Файл {args.file_path} не существует.")
