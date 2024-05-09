result = 12
while True:
    user_input = int(input('Введите число: '))
    if user_input > result:
        print('Попробуйте снова')
    elif user_input < result:
        print('Попробуйте снова')
    else:
        print('Поздравляю! Вы угадали!')
        break
