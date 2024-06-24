import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("dir_path", help=r"C:\Users\HP 745 G5\ST7\homework\eugene_okulik\data\logs")
parser.add_argument("words_count", type=int, help="How many words to take around the target word")
parser.add_argument("target_word", help="Searched text")
args = parser.parse_args()


dir_path = args.dir_path
target_word = args.target_word
search_words_count = args.words_count

file_list = os.listdir(dir_path)


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            yield line.strip()


def main():
    found_any_target = False
    for file_name in file_list:
        file_path = os.path.join(dir_path, file_name)

        row_number = 0
        for row in read_file(file_path):
            row_number += 1

            char_index = row.find(target_word)
            if char_index < 0:
                continue

            found_any_target = True
            char_index_start = char_index
            char_index_end = char_index + len(target_word) - 1
            shift = search_words_count * 50

            char_index_start = max(char_index_start - shift, 0)
            char_index_end = char_index_end + shift

            simplified_row = row[char_index_start:char_index_end]

            words = simplified_row.split(' ')
            try:
                word_index = words.index(target_word)
            except ValueError:
                continue

            words_found = words[max(word_index - search_words_count, 0):word_index + search_words_count + 1]
            words_found = ' '.join(words_found)

            print(f"File: {file_name} - Row #{row_number}. Found: '{words_found}'")

    if not found_any_target:
        print(f"Target word '{target_word}' not found in any file.")


main()
