from flower import Flower


class Lily(Flower):

    def __init__(self, price, color, shelf_life):
        super().__init__('Lily', price, color, shelf_life)
