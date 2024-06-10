import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
dir_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_13')
file_path = os.path.join(dir_path, 'data.txt')

with open(file_path, 'r', encoding='utf-8') as my_file:
    data = my_file.read()
    for upper_word in data:
        if upper_word.isupper():
            print(upper_word, end='')
