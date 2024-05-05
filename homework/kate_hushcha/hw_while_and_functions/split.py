
one = 'результат операции: 42'
two = 'результат операции: 54'
three = 'результат работы программы: 209'
four = 'результат: 2'

def digit(num):
    return int(num.split()[-1]) + 10

print(digit(one))
print(digit(two))
print(digit(three))
print(digit(four))
