from flower import Flower


class Tulip(Flower):

    def __init__(self, price, color, shelf_life):
        super().__init__('Tulip', price, color, shelf_life)
