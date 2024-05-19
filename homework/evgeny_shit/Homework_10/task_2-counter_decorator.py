def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.pop('count', 1)  # Retrieving 'count' from kwargs with default value 1
        for _ in range(count):
            func(*args, **kwargs)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


#  Use @repeat_me with parameter count=2
def repeat_me2(count=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(count):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat_me2(count=2)
def example2(text):
    print(text)


example2('print me 2')
