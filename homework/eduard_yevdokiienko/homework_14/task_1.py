import datetime

date_format = '%d/%m/%Y'

while True:
    user_input = input('Please type your birth date: ')
    try:
        birth_date = datetime.datetime.strptime(user_input, date_format)
        current_date = datetime.datetime.now()
        age_in_days = (current_date - birth_date).days
        print(f'Age in days: {age_in_days}')
        break
    except ValueError:
        print('Invalid date format. Please enter the date in the format: dd/mm/yyyy')
