num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))


def strange_decor(func):
    def wrapper(first, second):
        if first < 0 or second < 0:
            return func(first, second, '*')
        elif first == second:
            return func(first, second, '+')
        elif first > second:
            return func(first, second, '-')
        else:
            return func(first, second, '/')
    return wrapper


@strange_decor
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second
    else:
        return 'Wrong operator'


print(calc(num_1, num_2))
