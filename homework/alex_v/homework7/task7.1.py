from random import randrange

random_number = randrange(10)
print(random_number)

while num := int(input("Угадай число от 0 до 9 -> ")) != random_number:
    print("Не угадал. Пробуй ещё")
print(f"Вау! Поздравляю! Ты угадал число {random_number}")
