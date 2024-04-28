my_dict = {
    'tuple': (2, 4, 6.5, None, False),
    'list': [1, 3, 'text', False, 8],
    'dict': {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e'},
    'set': {5, 7, True, 10, 'text'}
}
print(my_dict['tuple'][-1])

my_dict['list'].append(50)
my_dict['list'].pop(2)

my_dict['dict']['i am a tuple'] = 50
my_dict['dict'].pop('1')

my_dict['set'].add(50)
my_dict['set'].pop()

print(my_dict)
