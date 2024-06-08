import sys
import os
import datetime

sep = '/' if sys.platform in ['linux', 'darwin'] else '\\'

url_begining = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(f'{url_begining}{sep}eugene_okulik{sep}hw_15{sep}data.txt', 'r', encoding='utf-8') as eugenes_file:
    data = eugenes_file.readlines()

print(data)

date = datetime.datetime.strptime(data[0][3:29], '%Y-%m-%d %H:%M:%S.%f')
print(date + datetime.timedelta(days=7))

date = datetime.datetime.strptime(data[1][3:29], '%Y-%m-%d %H:%M:%S.%f')
print(date.strftime('%A'))

date = datetime.datetime.strptime(data[2][3:29], '%Y-%m-%d %H:%M:%S.%f')
print((datetime.datetime.now() - date).days)
