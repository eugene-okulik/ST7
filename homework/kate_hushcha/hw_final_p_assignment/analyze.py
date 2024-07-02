import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("path", help="Your file path")
parser.add_argument("--word", help="The word")
parser.add_argument("--valid", help="search for date", action="store_true")
args = parser.parse_args()


def a_file(file_path, search_word):
    try:
        with open(file_path, encoding='utf-8') as file:
            user_file = file.read()
        file_lines = user_file.split('\n')
        for line_number, line in enumerate(file_lines, start=1):
            if search_word in line:
                words_count = line.split()
                w_index = words_count.index(args.word)
                before_w = w_index - 5
                after_w = w_index + 5
                print(f'File: {file_path}, line: {line_number},')
                print(f'words: {" ".join(words_count[before_w:after_w])}')
        if search_word not in line:
            print('Word not found')

    except ValueError:
        print('There is an error occured')


if os.path.isfile(args.path):
    a_file(args.path, args.word)
elif os.path.isdir(args.path):
    for file_name in os.listdir(args.path):
        file_path = os.path.join(args.path, file_name)
        if os.path.isfile(file_path):
            a_file(file_path, args.word)
else:
    print('The path is wrong')
