def repeat_me(count):
    def decor(func):
        def wrapper(*args):
            for i in range(count):
                func(*args)

        return wrapper

    return decor


@repeat_me(3)        # count
def example(text):
    print(text)


example('print me')
