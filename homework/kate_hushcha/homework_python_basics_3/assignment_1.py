
my_dict = {'tuple': (2, 12, 22, 32, 42, 52), 'list': ['two', 2, 'five', 5, 2.5]}
my_dict['dic'] = {'boy': 1, 'girl': 2, 'mom': 4, 'dad': 5, 'family': 'together'}
my_dict['set'] = {909, 'Nine', 911, 'help', 'reality'}

print(my_dict['tuple'][-1])

my_dict['list'].append('more')
my_dict['list'].pop(1)
# print(my_dict['list'])

my_dict['dic'][('i am a tuple',)] = 'therefore i am a flower called tulip'
my_dict['dic'].pop('girl')
# print(my_dict['dic'])

my_dict['set'].add('nine o nine')
my_dict['set'].remove('help')
# print(my_dict['set'])

print(my_dict)
