from datetime import datetime


def calc_birth():
    while True:
        user_input = input('Введите вашу даду рождения, например дд.мм.гггг-23.07.1995: ')
        try:
            day = datetime.strptime(user_input, '%d.%m.%Y')
            age = (datetime.now() - day).days
            print(f"Ваш возраст в днях: {age}")
            break
        except ValueError:
            print('Не верный фармат ввода, введите формат как в примере *после дня и месяца ставиться (.)'
                  ' (дд.мм.гггг-23.07.1995)')


calc_birth()
