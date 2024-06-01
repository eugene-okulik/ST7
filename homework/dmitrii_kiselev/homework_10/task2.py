def repeat_me(func):

    def wrapper(*args, **kwargs):
        for i in range(kwargs['count']):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)
