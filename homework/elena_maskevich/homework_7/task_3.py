first_line = 'результат операции: 42'
second_line = 'результат операции: 514'
third_line = 'результат работы программы: 9'
forth_line = 'результат: 2'


def calc(a):
    ind = a.find(':')
    new_number = int(a[(ind+2):]) + 10
    return new_number


print(calc(first_line) + calc(second_line) + calc(third_line) + calc(forth_line))