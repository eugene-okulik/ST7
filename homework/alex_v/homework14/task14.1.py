import datetime

birth_day = input("Enter the date when you was born ")

try:
    python_date = datetime.datetime.strptime(birth_day, '%d.%m.%Y')
    present_day = datetime.datetime.now()
    difference = present_day - python_date
    print(python_date)
    print(f'Your current age in days is {difference} ')
except ValueError:
    print('Wrong birthday format entering. Try this one -> DD.MM.YYYY')
