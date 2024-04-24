import random

my_dict = {'tuple': (1, 2, 3, 4, 5),
           'dict': {'first': 11, 'second': 22, 'third': 33, 'fourth': 44, 'fifth': 55},
           'list': [10, 20, 30, 40, 50],
           'set': {'one', 'two', 'three', 'four', 'five'}
           }

#  Tuple action.
print(f"The last element of the tuple \n{my_dict['tuple'][-1]}\n")

#  List action
my_dict['list'].append(60)
my_dict['list'].pop(1)

print(f"Adding the value '60' to the list and deleting the 2nd item\n{my_dict['list']}\n")

#  Dict action
my_dict['dict'][('i am a tuple',)] = (111,)
random_key = random.choice(list(my_dict['dict'].keys()))
del my_dict['dict'][random_key]

print(f"Adding a key ('i am a tuple,') with the value '(111,)' and deleting a random element \n{my_dict['dict']}\n")

#  Set action
my_dict['set'].add('six')
my_dict['set'].pop()
dict_set = my_dict['set']

print(f"Adding the value 'six' and deleting the value 'three'\n{my_dict['set']}\n")

print(f'The entire dictionary "my_dict" \n{my_dict}')
