def fibonacci():
    fibonacci_number, fibonacci_number_next = 0, 1
    while True:
        yield fibonacci_number
        fibonacci_number, fibonacci_number_next = fibonacci_number_next, fibonacci_number + fibonacci_number_next


result_list, count = [5, 200, 1000, 100000], 1

for x in fibonacci():
    if count in result_list:
        print(x)
    count += 1
    if count > max(result_list):
        break
