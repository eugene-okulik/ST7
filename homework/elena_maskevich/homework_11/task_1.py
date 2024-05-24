# Обработка даты
# Дана такая дата: "Jan 15, 2023 - 12:05:33"
# Преобразуйте эту дату в питоновский формат, после этого:
# 1. Распечатайте полное название месяца из этой даты
# 2. Распечатайте дату в таком формате: "15.01.2023, 12:05"

import datetime

my_date = "Jan 15, 2023 - 12:05:33"
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
print(python_date)
human_month = python_date.strftime("month: %B")
print(human_month)
new_date = python_date.strftime("%d.%m.%Y, %H:%M")
print(new_date)
