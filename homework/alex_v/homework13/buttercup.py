from abstract_flower import Flower


class Buttercup(Flower):
    def __init__(self, color, price, lifespan, stem_length):
        super().__init__("Buttercup", color, price, lifespan, stem_length)
