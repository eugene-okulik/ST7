def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()

count = 0

for num in fibonacci_generator():
    print(num) if count in [4, 199, 999, 99999] else None
    count = count + 1
    if count > 99999:
        break
