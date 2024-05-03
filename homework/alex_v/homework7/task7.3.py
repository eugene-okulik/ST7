operation_one = "результат операции: 42"
operation_two = "результат операции: 514"
operation_three = "результат операции: 9"


def add_number(number):
    print(int(number.split(': ')[-1]) + 10)


add_number(operation_one)
add_number(operation_two)
add_number(operation_three)
