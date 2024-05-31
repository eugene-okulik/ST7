class Flower:
    alive = True

    def __init__(self, name, color, price, length, freshness, lifetime):
        self.name = name
        self.color = color
        self.price = price
        self.length = length  # cm
        self.freshness = freshness
        self.lifetime = lifetime  # days


class RedRose(Flower):
    def __init__(self, price, length, freshness):
        super().__init__('Red Rose', 'red', price, length, freshness, 14)


class YellowTulip(Flower):
    def __init__(self, price, length, freshness):
        super().__init__('Yellow Tulip', 'yellow', price, length, freshness, 7)


class WhiteOrchid(Flower):
    def __init__(self, price, length, freshness):
        super().__init__('White Orchid', 'white', price, length, freshness, 10)


rose = RedRose(50, 80, 5)
tulip = YellowTulip(25, 40, 3)
orchid = WhiteOrchid(60, 15, 7)


class Bouquet:
    def __init__(self):
        self.price = 0
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)
        self.price += flower.price

    def get_lifetime(self):
        if not self.flowers:
            return 0
        total_lifetime = sum(flower.lifetime for flower in self.flowers)
        return total_lifetime / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key= lambda flower: flower.freshness)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_length(self):
        self.flowers.sort(key=lambda flower: flower.length)

    def sort_by_price(self, ):
        self.flowers.sort(key=lambda flower: flower.price)


bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(orchid)

print(f'Bouquet price: {bouquet.price}')
print(f'Bouquet lifetime: {bouquet.get_lifetime()}')