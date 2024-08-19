class MyClass:
    token = None

    def set_token(self, value):
        self.token = value


obj1 = MyClass()
print(obj1.token)
obj1.set_token('qqqqqqqqq')
print(obj1.token)
obj2 = MyClass()
print(obj2.token)
