# Напишите программу: Есть функция которая делает одну из арифметических операций с переданными ей числами (числа и
# операция передаются в аргументы функции). Программа спрашивает у пользователя 2 числа (вне функции)
#
# Создайте декоратор, который декорирует функцию calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def select_operation(func):

    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        func(first, second, operation)

    return wrapper


@select_operation
def calc(first, second, operation):
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(second - first)
    elif operation == '*':
        print(first * second)
    else:
        print(first / second)


calc(first=int(input()), second=int(input()))
