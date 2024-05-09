
def fibonacci():
    first_num = 0
    second_num = 1
    while True:
        yield first_num
        first_num = second_num
        second_num = first_num + second_num

                
count = 0
for num in fibonacci():
    if count == 4:
        print(num)
    count += 1
    if count == 199:
        print(num)
    if count == 999:
        print(num)
    if count == 99999:
        print(num)
        break
