import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("file_path", help='D:/Python/projectTumanov/st7/homework/eugene_okulik/data/logs')
parser.add_argument("--text", help="WARN", required=True)

args = parser.parse_args()

if os.path.exists(args.file_path):
    with open(args.file_path, encoding='utf-8') as file:
        found = False
        for line_number, line in enumerate(file, start=1):
            if args.word in line:
                found = True
                word_index = line.find(args.word)
                five_symb_before = max(0, word_index - 5)
                five_symb_after = min(len(line), word_index + len(args.word) + 5)
                print(f"{line_number}: ...{line[five_symb_before:five_symb_after]}...")
        if not found:
            print('Слово не найдено')
else:
    print(f"Файла {args.file_path} Не существует.")
