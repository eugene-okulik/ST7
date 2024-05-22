def limited_calls_decorator(*limit):

    def wrapper(function):

        def called(*args, **kwargs):
            count = 0
            while count < limit[0]:
                function(*args, **kwargs)
                count += 1
            print('Лимит вызовов превышен')
            return None
        return called
    return wrapper


@limited_calls_decorator(3)
def my_func():
    print('Функция выполняется')


my_func()
