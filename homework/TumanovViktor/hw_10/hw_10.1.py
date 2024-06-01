def finish_me(func):
    def wrapper(text):
        func(text)
        print()
        print('finished')

    return wrapper


@finish_me
def example(a):
    print(a)


example('print me')
