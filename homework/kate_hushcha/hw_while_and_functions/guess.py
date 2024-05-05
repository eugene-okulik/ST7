right_number = 8

while True:
    user_guess = int(input('Guess the number:\n'))
    if user_guess != right_number:
        print('Try Again!')
    if user_guess == right_number:
        print('Great Job! You are right.')
        break
    