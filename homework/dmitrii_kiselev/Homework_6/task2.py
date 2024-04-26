for number in range(1, 101):
    if not number%3 and not number%5:
        print('FuzzBuzz')
    elif not number % 3:
        print('Fuzz')
    elif not number % 5:
        print('Buzz')
    else:
        print(number)
