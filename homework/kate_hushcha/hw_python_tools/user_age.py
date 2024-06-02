import datetime


def dob():
    try:
        user_birthday = input('What is you DoB?\n')
        now_date = datetime.datetime.now()
        p_user_bd = datetime.datetime.strptime(user_birthday, '%m/%d/%Y')
        user_age = now_date - p_user_bd
    except ValueError:
        print('Try the following format: mm/dd/yyyy')
    else:
        print(f'You are {user_age.days} days old')


dob()
