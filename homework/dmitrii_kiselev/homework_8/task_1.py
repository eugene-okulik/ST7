def fibonacci():
    fibonacci_number_previous, fibonacci_number_pre_previous = 0, 1
    while True:
        fibonacci_number = fibonacci_number_previous + fibonacci_number_pre_previous
        yield fibonacci_number
        fibonacci_number_pre_previous = fibonacci_number_previous
        fibonacci_number_previous = fibonacci_number


result_list, count = [5, 200, 1000, 100000], 2

for x in fibonacci():
    if count in result_list:
        print(x)
    count += 1
    if count > 100000:
        break
