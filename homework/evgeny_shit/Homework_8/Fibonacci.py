import sys


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(index):
    fib_gen = fibonacci()
    for _ in range(index):
        number = next(fib_gen)
    return number


sys.set_int_max_str_digits(50000)

print(f"Num 5: {get_fibonacci_number(5)}")
print(f"Num 200: {get_fibonacci_number(200)}")
print(f"Num 1000: {get_fibonacci_number(1000)}")
print(f"Num 100000: {get_fibonacci_number(100000)}")
