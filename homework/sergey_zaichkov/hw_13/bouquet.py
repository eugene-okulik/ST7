from tulip import Tulip
from lily import Lily


class Bouquet:
    def __init__(self):
        self.__flowers_bouquet = []

    @property
    def price(self):
        return sum(float(flower.price) for flower in self.__flowers_bouquet)

    @property
    def expiry_term(self):
        return sum(float(flower.shelf_life) for flower in self.__flowers_bouquet) / len(self.__flowers_bouquet)

    def add_flowers(self, *flowers):
        for flower in flowers:
            self.__flowers_bouquet.append(flower)

    def get_flowers(self):
        return self.__flowers_bouquet

    def sort_flowers_by(self, value):
        try:
            return sorted(self.__flowers_bouquet, key=lambda x: getattr(x, value))
        except AttributeError:
            return f"'{value}' is invalid parameter for sorting"

    def get_flowers_by_color(self, color):
        return list(filter(lambda flower: flower.color == color, self.__flowers_bouquet))


tulip = Tulip(3, 'pink', 8)
lily = Lily(2, 'white', 9)
tulip_2 = Tulip(4, 'white', 6)
lily_2 = Lily(5, 'red', 7)

bouquet = Bouquet()
bouquet.add_flowers(tulip, lily, tulip_2)
bouquet.add_flowers(lily_2)

print(bouquet.get_flowers())
print(bouquet.price)
print(bouquet.expiry_term)
print(bouquet.sort_flowers_by('name'))
print(bouquet.sort_flowers_by('price'))
print(bouquet.sort_flowers_by('shelf_life'))
print(bouquet.sort_flowers_by('color'))
print(bouquet.sort_flowers_by('smell'))
print(bouquet.get_flowers_by_color('white'))
