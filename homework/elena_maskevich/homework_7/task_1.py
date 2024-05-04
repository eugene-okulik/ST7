# secret_number = input('Введете секретное число: ')
# suggested_number = input('Угадайте секретное число: ' )
# if suggested_number == secret_number:
#     print('Поздравляю! Вы угадали!')
# else:
#     while True:
#         user_input = input('Попробуйте снова ')
#         if user_input == secret_number:
#             print('Поздравляю! Вы угадали!')
#             break

secret_number = input('Введете секретное число: ')
suggested_number = input('Угадайте секретное число: ' )
if suggested_number == secret_number:
    print('Поздравляю! Вы угадали!')
else:
    while True:
        if user_input := input('Попробуйте снова ') == secret_number:
            print('Поздравляю! Вы угадали!')
            break


