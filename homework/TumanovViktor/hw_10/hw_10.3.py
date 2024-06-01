first = int(input('Введите число'))
second = int(input('Введите число'))


def decor(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif first < second:
            return func(first, second, '/')

    return wrapper


@decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    if operation == '-':
        return first - second
    if operation == '*':
        return first * second
    return first / second


res = calc(first, second)
print(res)
