from abstract_flower import Flower


class Rose(Flower):
    def __init__(self, color, price):
        super().__init__("Rose", color, price)
