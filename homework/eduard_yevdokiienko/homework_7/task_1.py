char = 35

while True:
    user_input = input('Guess the number:')
    user_input = int(user_input)
    if user_input != char:
        print('Try again!')
        continue
    elif user_input == char:
        print('Congratulations! You guessed!')
        break
    print(user_input)
