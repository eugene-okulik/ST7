import os
import datetime

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(f'projetc root is {project_root}')

task_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_15')
file_path = os.path.join(task_path, 'data.txt')

print(file_path)

with open(file_path, encoding='utf-8') as my_data:
    data = my_data.readlines()  # read the file with data
    print(f'initial data text -> {data} ')  # show the file data
    dates = []
    for string in data:
        parts = string.split(' - ')  # between data and task explanation
        print(f'first string of text -> {parts[0]}')  # show first string
        date_string = parts[0][3:]  # get data w/o garbage stuff
        date_time = datetime.datetime.fromisoformat(date_string)  # datetime string parsing
        print(date_time)
        dates.append(date_time)
date1, date2, date3 = dates

first_date = date1 + datetime.timedelta(weeks=1)
print(first_date)

second_date = date2.strftime('%B')
print(second_date)

third_date = datetime.datetime.now() - date3

print(third_date)
