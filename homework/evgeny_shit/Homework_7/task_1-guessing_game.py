import random

answer = random.randint(1, 100)

print("See if you can guess what number between 1 and 100 I'm guessing? \nYou have 10 tries. \nI'll give you hints.\n")

attempts = 10

while attempts > 0:
    try:
        if (guess := int(input(f"Try (1 to 100) you have {attempts} attempts left: \n"))) == answer:
            print(f"Congratulations! You guessed it on the {11 - attempts} try!")
            break
        elif guess < answer:
            print("Your guess is too LOW. Try again\n")
        else:
            print("Your guess is too HIGH. Try again\n")
    except ValueError:
        print("Please enter an integer\n")
        continue

    attempts -= 1

else:
    print("Sorry! You ran out of guesses. Good luck next time!\n")
