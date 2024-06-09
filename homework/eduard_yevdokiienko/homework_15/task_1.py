import datetime
import os

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
dir_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_15')
file_path = os.path.join(dir_path, 'data.txt')

with open(file_path, 'r', encoding='utf-8') as my_file:
    data = my_file.readlines()
    print(data)

dates = []

for line in data:
    lines = line.split()
    date_start = line.find(' ') + 1
    date_end = line.find(' -')
    dates.append(line[date_start:date_end])
    # print(dates)

date_1 = dates[0]
date_2 = dates[1]
date_3 = dates[2]
# print(date_1, date_2, date_3)

python_date_1 = datetime.datetime.strptime(date_1, '%Y-%m-%d %H:%M:%S.%f')
python_date_2 = datetime.datetime.strptime(date_2, '%Y-%m-%d %H:%M:%S.%f')
python_date_3 = datetime.datetime.strptime(date_3, '%Y-%m-%d %H:%M:%S.%f')

task_date_1 = python_date_1 + datetime.timedelta(days=7)
task_date_2 = python_date_2.strftime('%A')
task_date_3 = datetime.datetime.now() - python_date_3

print(f'A week later: {task_date_1};', f'Day of the week: {task_date_2};', f'Days ago: {task_date_3}.')
