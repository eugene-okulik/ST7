my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['one', 'two', 'three', 'four', 'five'],
    'dict': {'name': 'Sergey', 'lastname': 'Zaichkov', 'age': 36, 'city': 'SPB', 'job_title': 'Fullstack QA'},
    'set': {6, 7, 8, 9, 0}
}

# TUPLE
print(my_dict['tuple'][-1])

# LIST
my_dict['list'].append('six')
my_dict['list'].pop(1)  # del my_dict['list'][1]

# DICT
my_dict['dict']['i am a tuple'] = (1, 2, 3)
my_dict['dict'].pop('age', 'Key not found')  # del my_dict['dict']['age']

# SET
my_dict['set'].add(666)
my_dict['set'].discard(0)  # my_dict['set'].remove(0)

print(my_dict)
