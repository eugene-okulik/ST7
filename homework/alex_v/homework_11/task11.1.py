import datetime


my_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
month_date = python_date.strftime("%B")
other_format = python_date.strftime("%d.%m.%Y, %H:%M")
print(python_date)
print(month_date)
print(other_format)