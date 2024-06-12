class Flower:
    def __init__(self, name, color, price, lifespan, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.lifespan = lifespan
        self.stem_length = stem_length

    def __str__(self):
        print(f"{self.name}, {self.color}, {self.price},{self.lifespan},{self.stem_length}")
