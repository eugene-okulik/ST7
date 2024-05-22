
first = int(input('Enter the first number:\n'))
second = int(input('Enter the second number:\n'))


def operation_func(function):
    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first < 0 or second < 0:
            operation = '*'
        elif first > second:
            operation = '-'
        elif first < second:
            operation = '/'

        return function(first, second, operation)

    return wrapper


@operation_func
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(round(calc(first, second), 2))
