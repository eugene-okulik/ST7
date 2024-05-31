# import json


# my_file = open('data.txt', 'r', encoding='utf-8')
# data = my_file.read()
# data = json.loads(data)
# print(data)
# my_file.close()

with open('data.txt', 'r', encoding='utf-8') as my_file:
    print(type(my_file))
    data = my_file.read()


print(data)

with open('data1.txt', 'w', encoding='utf-8') as my_file:
    my_file.write('AAAAAAAAAAAAAAAAAAAAAA')


with open('data1.txt', 'a', encoding='utf-8') as my_file:
    my_file.write('WWWWWWWWWWWWW')
