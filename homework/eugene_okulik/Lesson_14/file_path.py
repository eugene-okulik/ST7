import os
import sys

dir_path = os.path.dirname(__file__)
print(os.getcwd())


# separator = '/' if sys.platform in ['linux', 'darwin'] else '\\'
# aa = 'McDonald\'s'

file_path = os.path.join(dir_path, 'data.txt')


with open(file_path, 'r', encoding='utf-8') as my_file:
    print(type(my_file))
    data = my_file.read()
    print(data)
