# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число
import sys
sys.set_int_max_str_digits(0)


def fibonachi(a):
    number_1 = 0
    number_2 = 0
    fib = 0
    for k in range(a):
        if number_2 == 0:
            yield 0
            number_2 += 1
        if number_2 == 1:
            fib = number_1 + number_2
            yield 1
            if fib != 1:
                yield fib
            number_1, number_2 = number_2, fib
        if number_2 > 1:
            fib = number_1 + number_2
            yield fib
            number_1, number_2 = number_2, fib


a = fibonachi(100000)
# print(a)
# for i in a:
#     print(i)

count = 0
for elem in a:
    count += 1
    if count == 5 or count == 200 or count == 1000 or count == 100000:
        print(elem)
