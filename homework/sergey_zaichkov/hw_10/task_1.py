def finish_me(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('finished')
    return wrapper


@finish_me
def greeter(name):
    print(f"Hello, {name}")


greeter('Sergey')
