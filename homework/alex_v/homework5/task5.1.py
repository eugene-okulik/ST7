my_dict = {
    'tuple': ('int', 'float', 'double', 'string', 'boolean'),
    'list': [1, 2, 3, 4, 5],
    'dict': {'name': 'alex', 'surname': 'v', 'sex': 'male', 'position': 'java_aqa', 'place': 'Krakow'},
    'set': {'epam', 'exadel', 'godel', 'panda_doc', 'anderson'}
}
print(my_dict['tuple'][-1])
my_dict['list'].append(6)
my_dict['list'].pop(2)
my_dict['dict']['expectation_salary'] = 5000
my_dict[('i am a tuple,')] = 'hate tuple'
my_dict['dict'].pop('position')
my_dict['set'].add('flo')
my_dict['set'].pop()
print(my_dict)
