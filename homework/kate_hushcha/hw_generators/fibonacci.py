
def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        result = first_num + second_num
        first_num = second_num
        second_num = result


count = 0
for num in fibonacci():
    if count == 4:
        print(num)
    if count == 199:
        print(num)
    if count == 999:
        print(num)
    if count == 99999:
        print(num)
        break
    count += 1
