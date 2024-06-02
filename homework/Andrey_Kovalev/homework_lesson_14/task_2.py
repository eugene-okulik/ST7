with open('D:/testST7/ST7/homework/eugene_okulik/hw_13/data.txt') as file:
    for i in file:
        for char in i:
            if char.isupper():
                print(char, end='')
