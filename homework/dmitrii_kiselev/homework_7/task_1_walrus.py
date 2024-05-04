import random

print('Введи два целых числа (диапазон, в котором будет игра)')
start, finish = int(input()), int(input())
random_number = random.randint(start, finish)

while (players_number := int(input(f'Введи свое число в диапазоне от {start} до {finish}:\n')) != random_number):
    print('попробуйте снова')

print('Поздравляю! Вы угадали!')
