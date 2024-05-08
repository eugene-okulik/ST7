import sys


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(index, generator):
    for _ in range(index):
        number = next(generator)
    return number


fib_gen = fibonacci()

# Устанавливаем максимальное количество цифр, которое может быть представлено в строке для int, т.к. в Python версии
# 3.10 и выше, максимальное количество цифр для строковых преобразований целых чисел по умолчанию установлено в 4300
# цифр
sys.set_int_max_str_digits(50000)

desired_numbers = [5, 200, 1000, 100000]
previous_number = 0

for current_number in desired_numbers:
    steps = current_number - previous_number
    print(f"Fibonacci number {current_number} : {get_fibonacci_number(steps, fib_gen)}")
    previous_number = current_number
