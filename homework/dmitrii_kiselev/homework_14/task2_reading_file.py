import sys
import os

sep = '/' if sys.platform in ['linux', 'darwin'] else '\\'

# к сожалению, не нашел лучшего решения, пришлось как все сисывать это решение))
# протестировать на линукс или маке не смог
url_begining = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(f'{url_begining}{sep}eugene_okulik{sep}hw_13{sep}data.txt', 'r', encoding='utf-8') as eugenes_file:
    data = eugenes_file.readlines()

for line in data:
    for symbol in line:
        if symbol not in (' ', '\n') and symbol == symbol.upper():
            print(symbol, end='')
