import random

rand_num = random.randint(0, 9)
print(rand_num)
while user_answer := int(input("Guess the number from 0 to 9\n")) != rand_num:
    print("Try again")

print("Congratulations! You guessed!")
