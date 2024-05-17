def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second if second != 0 else 'Error: Division by zero'
    else:
        return 'Invalid operation'


def operation_control(func):
    def wrapper(first, second):
        if second == 0 and first != 0:
            operation = '/'
        elif first < 0 or second < 0:
            operation = '*'
        elif first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        else:
            operation = '/'
        return func(first, second, operation)

    return wrapper


@operation_control
def controlled_calc(first, second, operation):
    return calc(first, second, operation)


while True:
    first_input = input("Enter first number (or 'stop' to exit): ")
    if first_input.lower() == 'stop':
        break

    second_input = input("Enter second number (or 'stop' to exit): ")
    if second_input.lower() == 'stop':
        break

    try:
        first_number = float(first_input)
        second_number = float(second_input)
    except ValueError:
        print("Error: Please enter valid numbers.")
        continue

    result = controlled_calc(first_number, second_number)
    if isinstance(result, str):  # Check for division by zero or other errors
        print(f"Result: {result}\n")
    else:
        print(f"Result: {result:.2f}\n")
