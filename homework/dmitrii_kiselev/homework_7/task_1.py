import random

print('Введи два целых числа (диапазон, в котором будет игра)')
start, finish = int(input()), int(input())
random_number = random.randint(start, finish)

players_number = int(input(f'Начнем игру! Введи свое число в диапазоне от {start} до {finish}:\n'))

while players_number != random_number:
    print('попробуйте снова')
    players_number = int(input(f'Введи свое число в диапазоне от {start} до {finish}:\n'))

print('Поздравляю! Вы угадали!')
