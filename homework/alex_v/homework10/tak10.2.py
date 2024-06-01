def repeat_me(func):
    def wrapper(*args, **kwargs):
        count = kwargs.get('count', 1)
        for _ in range(count):
            func(*args)

    return wrapper


@repeat_me
def test_repeat_decor(text):
    print(text)


test_repeat_decor('print me', count=7)
