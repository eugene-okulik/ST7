import datetime

given_date = 'Jan 15, 2023 - 12:05:33'
right_date = datetime.datetime.strptime(given_date, '%b %d, %Y - %H:%M:%S')
final_date = right_date.strftime('%B')
print(final_date)

updated_date = right_date.strftime('%d.%m.%Y, %H:%M')
print(updated_date)
