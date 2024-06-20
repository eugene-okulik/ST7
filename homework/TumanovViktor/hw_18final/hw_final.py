import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help='D:/Python/projectTumanov/st7/homework/eugene_okulik/data/logs/')
parser.add_argument("--text", help="WARN", required=True)

args = parser.parse_args()

if os.path.exists(args.file_path):
    with open(args.file_path, encoding='utf-8') as file:
        found = False
        for line_number, line in enumerate(file, start=1):
            words = line.split()
            if args.text in words:
                found = True
                word_index = words.index(args.text)
                start_index = max(0, word_index - 5)
                end_index = min(len(words), word_index + 6)
                context = ' '.join(words[start_index:end_index])
                print(f"{line_number}: {context}")
        if not found:
            print('Слово не найдено')
else:
    print(f"Файла {args.file_path} Не существует.")
