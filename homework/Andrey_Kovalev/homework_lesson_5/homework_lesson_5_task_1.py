my_dict = {
    'truple': ('1', '2', '3', '4', '5'),
    'list': ['test', 'text', 'letter', 'read', 'book'],
    'dict': {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14},
    'set': {16, 17, 18, 19, 20}
}

print(my_dict['truple'][-1])

my_dict['list'].append('new_book')
my_dict['list'].pop(1)

my_dict['dict']['i am a tuple,'] = 'i love python'
my_dict['dict'].pop('b')

my_dict['set'].add(1312)
my_dict['set'].pop()

print(my_dict)