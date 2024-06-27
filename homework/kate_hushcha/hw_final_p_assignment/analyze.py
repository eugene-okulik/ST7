import argparse


parser = argparse.ArgumentParser()

parser.add_argument("file_path", help="Your file path")
parser.add_argument("--word", help="The word")
parser.add_argument("--valid", help="search for date", action="store_true")

args = parser.parse_args()

with open(args.file_path, encoding='utf-8') as file:
    user_file = file.read()

file_lines = user_file.split('\n')

for line_number, line in enumerate(file_lines, start=1):
    if args.word in line:
        words_count = line.split()
        w_index = words_count.index(args.word)
        before_w = w_index - 5
        after_w = w_index + 5
        print(words_count[before_w], words_count[w_index], words_count[after_w])
    else:
        print('Word is not found')
