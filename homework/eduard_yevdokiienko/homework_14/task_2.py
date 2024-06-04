import os

dir_path = 'homework/eugene_okulik/hw_13/'
file_path = os.path.join(dir_path, 'data.txt')
with open(file_path, 'r', encoding='utf-8') as my_file:
    data = my_file.read()
    for upper_word in data:
        if upper_word.isupper():
            print(upper_word, end='')
