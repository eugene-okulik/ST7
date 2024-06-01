import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(project_root)

task_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_13')
file_path = os.path.join(task_path, 'data.txt')
print(file_path)

with open(file_path, 'r', encoding='utf-8') as my_file:
    data = my_file.read()
    for elem in data:
        if elem.isupper():
            print(elem, end=' ')
