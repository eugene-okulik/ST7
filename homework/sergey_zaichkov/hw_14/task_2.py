import os
from pathlib import Path

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
file_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_13', 'data.txt')

with open(file_path) as f:
    data = f.read()

result = ', '.join(char for char in data if char.isupper())
print(result)
