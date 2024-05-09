def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibonacci = fibonacci_generator()

# Получение пятого числа Фибоначчи
fifth_number = next(fibonacci)
for _ in range(4):
    fifth_number = next(fibonacci)

print("Fifth number in Fibonacci sequence:", fifth_number)

# Получение 200-го числа Фибоначчи
for _ in range(195):  # Итерируем 200 - 5 раз, так как уже получили пятое число
    next(fibonacci)
two_hundredth_number = next(fibonacci)
print("Two hundredth number in Fibonacci sequence:", two_hundredth_number)

# Получение 1000-го числа Фибоначчи
for _ in range(795):  # Итерируем 1000 - 200 - 5 раз
    next(fibonacci)
thousandth_number = next(fibonacci)
print("Thousandth number in Fibonacci sequence:", thousandth_number)

# Получение 100000-го числа Фибоначчи
for _ in range(99795):  # Итерируем 100000 - 1000 - 200 - 5 раз
    next(fibonacci)
hundred_thousandth_number = next(fibonacci)
