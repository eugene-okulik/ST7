# it was difficult and I wouldn't repeat it in future

def repeat_me(**count):
    def wrapper(function):
        def called(*args, **kwargs):
            for i in range(count['count']):
                function(*args, **kwargs)
        return called
    return wrapper


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
