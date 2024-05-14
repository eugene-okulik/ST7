import sys
sys.set_int_max_str_digits(0)


def generate_fibonacci_numbers():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num1, num2 = num2, num1 + num2


gen = generate_fibonacci_numbers()

fib_num_positions = [5, 200, 1000, 100_000, 8, 1]
max_num_pos = max(fib_num_positions)

for num_pos, fib_num in enumerate(gen, start=1):
    if num_pos in fib_num_positions:
        print(f"In {num_pos} position: {fib_num}")
        if num_pos == max_num_pos:
            break
