def num_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


generation_num = num_fibonacci()

count = 0

for x in num_fibonacci():
    if count == 3:
        print(x)
    if count == 100:
        print(x)
    if count == 5000:
        print(x)
    if count == 10000:
        print(x)
    count += 1
    if count > 10000:
        break
