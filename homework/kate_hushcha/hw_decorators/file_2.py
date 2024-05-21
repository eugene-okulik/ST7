
def count(func):

    def wrapper(data, number):
        for _ in range(number):
            func(data)

    return wrapper

@count
def routine(text):
    print(text)

routine('Good Morning!', number=3)
