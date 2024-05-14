my_dict = {
    'tuple': (10, 25, 35, 44, 57),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {'name': 'Anton', 'lastname': 'Bagrov', 'age': 44, 'city': 'Krasnogorsk', 'job_title': 'manual_QA'},
    'set': {6, 7, 8, 9, 0}
}

# TUPLE - кортежи
print(my_dict['tuple'][-1])  # -1 последний элемент, -2 предпоследний и тд

# LIST - списки
my_dict['list'].append('last')  # добавление последнего элемента ('last')
my_dict['list'].pop(1)  # удаление второго элемента списка ('two')

# DICT - словарь
my_dict['dict'][('i am a tuple',)] = (33, )
my_dict['dict'].pop('city',)  # удаление элемента (ключа) city

# SET - множество
my_dict['set'].add(8170)
my_dict['set'].discard(8)  # удаление элемента 8

print(my_dict)
