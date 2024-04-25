my_dict = {'tuple': (1, 3, 'one', 2.33, True), 'list': [1, 'one', None, False, 4.4], 'dict': {'one': 3, 'two': 39, 'my':
           True, 'double': 78, 'car': False}, 'set': {1, 5, 'double', 4.5, 'running'}}
print(my_dict)

tuple1, list1, dict1, set1 = my_dict
my_tuple = my_dict[tuple1]
# выведите на экран последний элемен tuple
print(my_tuple[4])
# добавьте в конец списка еще один элемент
# удалите второй элемент списка
my_list = list(my_dict[list1])
my_list.append('appended')
my_list.pop(1)
print(my_list)
# добавьте элемент с ключом ('i am a tuple',) и любым значением
# удалите какой-нибудь элемент
my_dict1 = my_dict[dict1]
my_dict1['i am a tuple'] = 'tuple'
del my_dict1['one']
print(my_dict1)
# добавьте новый элемент в множество
# удалите элемент из множества
my_set1 = my_dict[set1]
my_set1.add(4)
my_set1.pop()
print(my_set1)
print(my_dict)
