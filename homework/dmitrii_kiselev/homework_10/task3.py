def make_operator(func):

    def wrapper(*args):
        a, b = args
        if a < 0 or b < 0:
            return func(*args, '*')
        if a == b:
            return func(*args, '+')
        if a < b:
            return func(*args, '/')
        return func(*args, '-')
    return wrapper


@make_operator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    else:
        return first * second


print(calc(int(input()), int(input())))
