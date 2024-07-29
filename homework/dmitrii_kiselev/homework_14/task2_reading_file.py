import os


url_begining = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(os.path.join(url_begining, 'eugene_okulik', 'hw_13', 'data.txt'), 'r', encoding='utf-8') as eugenes_file:
    data = eugenes_file.readlines()

for line in data:
    for symbol in line:
        if symbol not in (' ', '\n') and symbol == symbol.upper():
            print(symbol, end='')
