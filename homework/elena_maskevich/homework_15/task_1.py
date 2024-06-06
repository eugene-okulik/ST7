# Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugeny_okulik/hw_15/data.txt
# Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл, находит в нём даты и делает
# с этими датами то, что после них написано. Опирайтесь на то, что структура каждой строки одинакова: сначала идет
# номер, потом дата, потом дефис и после него текст. У вас должен получиться код, который находит даты и для даты под
# номером один в коде должно быть реализовано то действие, которое написано в файле после этой даты. Ну и так далее для
# каждой даты. Текст задания, который написан после даты распознавать не нужно, просто напишите код, который выполняет
# указанное действие.

import os
import datetime

project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
task_path = os.path.join(project_root, 'homework', 'eugene_okulik', 'hw_15')
file_path = os.path.join(task_path, 'data.txt')

with open(file_path, encoding='utf-8') as data_file:
    data = data_file.read()

lines = data.split('\n')
dates_array = []
for elem in lines:
    start = elem.find(' ')
    end = elem.find(' -')
    dates_array.append(elem[start + 1:end])
print(dates_array)
first = dates_array[0]
first_p = datetime.datetime.strptime(first, '%Y-%m-%d %H:%M:%S.%f')
seven_days = datetime.timedelta(days=7)
now = datetime.datetime.now()
print(f'Прошло {(now - first_p).days} дней')
print(first_p + seven_days)
print(f'День недели - {first_p.strftime("%A")}')
