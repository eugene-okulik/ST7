import datetime

my_date = 'Jan 15, 2023 - 12:05:33'
python_date = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')

month = python_date.strftime('%B')
print(month)

new_date = python_date.strftime('%d.%m.%y, %H:%M')
print(new_date)
