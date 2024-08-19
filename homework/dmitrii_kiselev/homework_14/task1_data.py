import datetime


def user_age(data):
    try:
        calculated_data = datetime.datetime.strptime(data, '%d/%m/%Y')  # dd/mm/yyyy
        return (calculated_data - datetime.datetime.now()).days + 1
    except ValueError:
        print('Требуется формат даты: dd/mm/yyyy')
        return user_age(input('Введи корректную дату > '))


user_data = input('Введи дату > ')
print(f'Ваш возраст в днях: {-1 * user_age(user_data)}')
