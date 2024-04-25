my_dict = {'tuple': (1, 2, 3, 4, 5), 'list': [1, 2, 3, 4, 5],
           'dict': {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}, 'set': {1, 2, 3, 4, 5}}

print(my_dict['tuple'][-1])

my_dict['list'].append(6)
my_dict['list'].pop(1)  # надеюсь правильно понял про удаление второго элемента. Речь про человеческий второй

my_dict['dict'][('i am a tuple',)] = 'some value'
my_dict['dict'].pop(3)

my_dict['set'].add('6')
my_dict['set'].pop()

print(my_dict)
