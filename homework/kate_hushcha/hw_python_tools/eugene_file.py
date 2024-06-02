import os

file_path = 'C:\\Users\\kater\\ST7\\homework\\eugene_okulik\\hw_13\\data.txt'

with open(file_path, 'r', encoding='utf-8') as my_file:
    data = my_file.read()
    for letter in data:
        if letter.isupper():
            print(letter)
