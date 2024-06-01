first_input = int(input('Type a number'))
second_input = int(input('Type a number'))


def x(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, '+')
        elif first >= second:
            return func(first, second, '-')
        elif first <= second:
            return func(first, second, '/')
        elif first < 0 or second < 0:
            return func(first, second, '*')

    return wrapper


@x
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return second - first
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


print(calc(first_input, second_input))
