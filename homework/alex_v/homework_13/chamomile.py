from abstract_flower import Flower


class Chamomile(Flower):
    def __init__(self, color, price):
        super().__init__("Chamomile", color, price)
