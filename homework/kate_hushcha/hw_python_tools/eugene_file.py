import os

root_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

eugene_path = os.path.join(root_path, 'homework', 'eugene_okulik', 'hw_13')
file_path = os.path.join(eugene_path, 'data.txt')

with open(file_path, 'r', encoding='utf-8') as my_file:
    data = my_file.read()
    for letter in data:
        if letter.isupper():
            print(letter)
