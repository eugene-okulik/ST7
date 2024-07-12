class MyClass:
    token = None

    @classmethod
    def set_token(cls, value):
        cls.token = value


obj2 = MyClass()
obj1 = MyClass()
print(obj1.token)
obj1.set_token('qqqqqqqqq')
print(obj1.token)
print(obj2.token)
