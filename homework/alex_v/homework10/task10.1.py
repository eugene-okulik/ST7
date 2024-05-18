def finish_me(func):
    def wrapper(*args):
        func(*args)
        print('finished')

    return wrapper


@finish_me
def test_decor_func(text):
    print(text)


test_decor_func('print me')
