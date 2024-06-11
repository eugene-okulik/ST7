import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_13')
eugene_okulik = os.path.join(file_path, 'data.txt')


with open(eugene_okulik, encoding='utf-8') as my_file:
    for i in my_file:
        for char in i:
            if char.isupper():
                print(char, end='')
