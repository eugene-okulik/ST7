def repeat_me(func):
    def wrapper(*args, **kwargs):
        for _ in range(kwargs.pop('count', 1)):
            func(*args, **kwargs)
    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=3)


@repeat_me
def example2(text, name, pet=False):
    print(text, name, pet)


example2('hello', 'sergey', pet=True, count=2)
