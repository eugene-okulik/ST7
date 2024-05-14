# Напишите функцию-генератор, которая генерирует список чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

def feb_progression():
    a = 0
    b = 1
    while True:
        result = a + b
        yield result
        a = b
        b = result


count = 0
for x in feb_progression():
    if count == 5 or count == 200 or count == 1000 or count == 100000:
        print(x)
    count += 1
    if count > 100000:
        break
