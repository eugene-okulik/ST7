from abstract_flower import Flower


class Rose(Flower):
    def __init__(self, color, price, lifespan, stem_length):
        super().__init__("Rose", color, price, lifespan, stem_length)
