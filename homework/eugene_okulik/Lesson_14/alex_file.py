import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
alex_path = os.path.join(project_root, 'homework', 'alex_v')


file_path = os.path.join(alex_path, 'file.txt')


with open(file_path, 'r', encoding='utf-8') as my_file:
    print(type(my_file))
    data = my_file.read()
    print(data)
