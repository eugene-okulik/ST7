class Flower:
    def __init__(self, name, price, color, shelf_life):
        self.__name = name
        self.__price = price
        self.__color = color
        self.__shelf_life = shelf_life

    def __repr__(self):
        return f"{self.__name}(price={self.__price}, color={self.__color}, shelf_life={self.__shelf_life})"

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def color(self):
        return self.__color

    @property
    def shelf_life(self):
        return self.__shelf_life
