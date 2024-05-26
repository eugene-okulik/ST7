def operation_manager(func):
    def wrapper(first, second, operation=None):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first:
            operation = '/'
        if first < 0 or second < 0:
            operation = '*'
        return func(first, second, operation)
    return wrapper

@operation_manager
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        if second == 0:
            return 'Error: Division by zero'
        return first / second
    else:
        return 'Error: Invalid operation'


first = float(input("Введите первое число: "))
second = float(input("Введите второе число: "))


result = calc(first, second)
print("Результат:", result)
