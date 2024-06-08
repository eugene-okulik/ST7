from abstract_flower import Flower


class Chamomile(Flower):
    def __init__(self, color, price, lifespan, stem_length):
        super().__init__("Chamomile", color, price, lifespan, stem_length)
