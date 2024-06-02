class Flower:
    def __init__(self,name,color,price):
        self.name = name
        self.color = color
        self.price = price

    def __str__(self):
        print(f"{self.name}, {self.color}, {self.price}")