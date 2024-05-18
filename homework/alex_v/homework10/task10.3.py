def calc_decider(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        elif second > first:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')
        return func(first, second, '')

    return wrapper


@calc_decider
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second if second != 0 else 'Division by zero is forbidden'


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))

result = calc(first, second)

print(result)
