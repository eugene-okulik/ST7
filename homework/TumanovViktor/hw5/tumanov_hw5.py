my_dict = {}
my_dict['tuple'] = (1, 23, 'den', 'karamba', 'sliva')
my_dict['my_list'] = [1, 3, 6, 7, 'text', False, 'last', 'sdfsdf']
my_dict['my_list'].append(12)  # Добавление элемента
my_dict['my_list'].pop(1)  # Удаление второго элемента по индексу.
my_dict['dict'] = {'one': 'value1', 'two': 'value2', 'free': 'value3', 'four': 'value4', 'fife': 'value5'}
dicta = {'i am a tuple': 'Tumanov'}
my_dict['dict'].update(dicta)  # Добавление через соединения словарей.
my_dict['dict'].pop('one')  # Удаление элемента по ключ-значение. Так же можно удалить через del
my_dict['my_set'] = {1, 3, 6, 7, 'task', 'text', 'False', 3}
my_dict['my_set'].add('Новый элемент')  # добовляет элемент во множество
my_dict['my_set'].discard('False')  # pop удаляет эелементы в рандоме.Remove вызовет ошибку если во множестве нету
# элемента
print(my_dict['tuple'][-1])
print(my_dict['my_list'])
print(my_dict['dict'])
print(my_dict['my_set'])
print(my_dict)

# Задание 2

str1 = 'результат операции: 42'
index = str1.index(':')
# print(index)
s = str1[index + 2:]
res = int(s) + 10
print(res)

str2 = "результат операции: 514"
index1 = str2.index(':')
# print(index)
s = str2[index + 2:]
res2 = int(s) + 10
print(res2)

str3 = 'результат операции: 9'
index2 = str3.index(':')
# print(index)
s = str3[index + 2:]
res3 = int(s) + 10
print(res3)

# Задание 3

person = ['Viktor', 'Tum', 'Naro-Fomisk', '+1372829383739', 'Russia']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание 4

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
print('Students ', ', '.join(students), 'study these subjects:', ', '.join(subjects))
