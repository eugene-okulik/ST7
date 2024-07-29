import os
import datetime

url_begining = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

with open(os.path.join(url_begining, 'eugene_okulik', 'hw_15', 'data.txt'), 'r', encoding='utf-8') as eugenes_file:
    data = eugenes_file.readlines()

date = datetime.datetime.strptime(data[0][3:29], '%Y-%m-%d %H:%M:%S.%f')
print(date + datetime.timedelta(days=7))

date = datetime.datetime.strptime(data[1][3:29], '%Y-%m-%d %H:%M:%S.%f')
print(date.strftime('%A'))

date = datetime.datetime.strptime(data[2][3:29], '%Y-%m-%d %H:%M:%S.%f')
print((datetime.datetime.now() - date).days)
