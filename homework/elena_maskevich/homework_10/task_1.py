#Создайте универсальный декоратор, который можно будет применить к любой функции. Декоратор должен делать следующее:
# он должен распечатывать слово "finished" после выполнения декорированной функции.
def prettify_me(func):

    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('finished')

    return wrapper


@prettify_me
def yell(text):
    print(text.upper() + '!')


yell('my text')


