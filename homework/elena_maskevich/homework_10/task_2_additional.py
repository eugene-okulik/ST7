# Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор, который сможет обработать
# такой код:

import functools


def repeat_me(repeat):
    """Повторение выполнения кода"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(x):
            for i in range(repeat):
                print(f'{i+1}: ', end='')
                val = func(x)
            return val
        return wrapper
    return decorator


@repeat_me(repeat=20)
def example(text):
    print(text)


example('print me')
