def num_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


generation_num = num_fibonacci()

count = 0

for x in num_fibonacci():
    if count == 4:
        print(x)
    if count == 199:
        print(x)
    if count == 999:
        print(x)
    if count == 99999:
        print(x)
        break
    count += 1
