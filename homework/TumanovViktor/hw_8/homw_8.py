import sys

sys.set_int_max_str_digits(30000)


def febich():
    f1 = 0
    f2 = 1
    while True:
        yield f1
        f1, f2 = f2, f1 + f2


# print(febich(n))

count = 0

for num in febich():
    if count == 4:
        print('Вывод пятого числа:', num, end=' ')
        print()
    if count == 199:
        print('Вывод двухсотого числа:', num, end=' ')
        print()
    if count == 999:
        print('Вывод тысячного числа:', num, end=' ')
        print()
    if count == 99999:
        print('Вывод десятитысячного:', num, end=' ')
        break

    count += 1
