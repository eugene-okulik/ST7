from abstract_flower import Flower


class Tulip(Flower):
    def __init__(self, color, price, lifespan, stem_length):
        super().__init__("Tulip", color, price, lifespan, stem_length)
