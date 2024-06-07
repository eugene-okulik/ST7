class Flower:
    def __init__(self, name, color, stem_length, freshness, cost, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.freshness = freshness
        self.cost = cost
        self.lifespan = lifespan

    def __repr__(self):
        return (f"{self.name}(Color: {self.color}, Stem Length: {self.stem_length} cm, Freshness: {self.freshness} "
                f"days, Cost: {self.cost}, Lifespan: {self.lifespan} days)")


class Rose(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__('Розы', color, stem_length, freshness, cost, 7)


class Tulip(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__('Тюльпаны', color, stem_length, freshness, cost, 5)


class Lily(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__('Лилии', color, stem_length, freshness, cost, 10)


class Daisy(Flower):
    def __init__(self, color, stem_length, freshness, cost):
        super().__init__('Маргаритка', color, stem_length, freshness, cost, 6)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def find_flowers_by_attribute(self, attr, value):
        return [flower for flower in self.flowers if getattr(flower, attr) == value]

    def __repr__(self):
        return f"Bouquet({self.flowers})"


rose1 = Rose('Красный', 40, 2, 5)
tulip1 = Tulip('Желтый', 30, 1, 3)
lily1 = Lily('Белый', 50, 3, 7)
daisy1 = Daisy('Розовый', 25, 4, 2)


bouquet = Bouquet()
bouquet.add_flower(rose1)
bouquet.add_flower(tulip1)
bouquet.add_flower(lily1)
bouquet.add_flower(daisy1)


print(bouquet)

print(f"Общая стоимость букета: {bouquet.total_cost()}")

print(f"Через сколько завянет букет: {bouquet.average_lifespan()} days")

bouquet.sort_flowers('cost')
print(f"Сортировка по стоимости: {bouquet}")

yellow_flowers = bouquet.find_flowers_by_attribute('color', 'Yellow')
print(f"Желтые цветы в букете: {yellow_flowers}")
