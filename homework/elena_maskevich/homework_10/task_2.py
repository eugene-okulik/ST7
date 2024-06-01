# Создайте универсальный декоратор, который будет управлять тем, сколько раз запускается декорируемая функция

def repeat_me(func):

    def wrapper(x, count):
        for i in range(count):
            func(x)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=6)
