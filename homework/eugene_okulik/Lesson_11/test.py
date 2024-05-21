# import random
from random import random, randint, randrange, choice
# from random import *  - такое запрещено
# from data.data_file import var, calc
from data import data_file as dta
# from homework.alex_v.homework4 import task4

# print(random.random())
# print(random.randint(1, 2))
# print(random.randrange(1, 2))
# variants = ['ok', 2, True]
# print(random.choice(variants))
print(random())
print(randint(1, 2))
print(randrange(1, 2))
variants = ['ok', 2, True]
print(choice(variants))

print(dta.var)
dta.calc(2)