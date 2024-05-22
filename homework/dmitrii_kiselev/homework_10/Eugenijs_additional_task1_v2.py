# simple task like first main task

def before_after_decorator(func):

    def wrapper():
        print('Перед выполнением')
        func()
        print('После выполнения')

    return wrapper


@before_after_decorator
def my_func():
    print('Функция выполняется')


my_func()
