import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("file_path", help="Your file path")
parser.add_argument("--word", help="The word")
parser.add_argument("--valid", help="search for date", action="store_true")

args = parser.parse_args()

with open (args.file_path, encoding='utf-8') as file:
    user_file = file.read()

file_line = user_file.split('\n')

for line_number, line in enumerate(file_line, start=1):
    word_index = line.find(args.word)
    five_symb_before = word_index - 5
    five_symb_after = word_index + 5
    if args.word in line:
        print(line_number, five_symb_before, args.word, five_symb_after)
    else:
        print('Word is not found')
