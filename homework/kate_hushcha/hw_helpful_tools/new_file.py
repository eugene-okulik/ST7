
import os
import datetime

new_file_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
data_path = os.path.join(new_file_path, 'homework', 'eugene_okulik', 'hw_15')
file_path = os.path.join(data_path, 'data.txt')


with open(file_path, encoding='utf-8') as dates_file:
    date_f = dates_file.read()

lines = date_f.split('\n')

for line in lines:
    content = line.splitlines()
    first_del = line.split(' ', 1)[1]
    second_del = first_del.split(' - ')[0]
    date = datetime.datetime.strptime(second_del, "%Y-%m-%d %H:%M:%S.%f")
    if 'распечатать эту дату, но на неделю позже' in line:
        new_del = date + datetime.timedelta(days=7)
        print(new_del)
    elif 'распечатать какой это будет день недели' in line:
        day_of_week = date.weekday()
        print(day_of_week)
    elif 'распечатать сколько дней назад была эта дата' in line:
        date_today = datetime.datetime.now()
        date_in_days = date_today - date
        date_in_days_1 = date_in_days.days
        print(date_in_days_1)
