class Flowers(object):
    def __init__(self, name, cost, lifetime, color, stem_length):
        self.name = name
        self.cost = cost
        self.lifetime = lifetime
        self.color = color
        self.stem_length = stem_length

    def print_info(self):
        print(f'{self.name}, цена {self.cost}, время жизни {self.lifetime}')


class Bell(Flowers):
    def __init__(self, name, cost, lifetime, color, stem_length):
        super().__init__('Колокольчик', cost, lifetime, color, stem_length)


class Chamomile(Flowers):
    def __init__(self, name, cost, lifetime, color, stem_length):
        super().__init__('ромашка', cost, lifetime, color, stem_length)


class Peony(Flowers):
    def __init__(self, name, cost, lifetime, color, stem_length):
        super().__init__('пион', cost, lifetime, color, stem_length)


class Gerbera(Flowers):
    def __init__(self, name, cost, lifetime, color, stem_length):
        super().__init__('гербера', cost, lifetime, color, stem_length)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def count_price(self):
        sum_cost = sum(flower.cost for flower in self.flowers)
        return sum_cost

    def average_life(self):
        lifetime = [int(flower.lifetime[0]) for flower in self.flowers]
        avg_lifetime = sum(lifetime)/len(lifetime)

        print(f'Среднее время увядания {avg_lifetime}')

    def sort_by_color(self):
        sorted_color = sorted(self.flowers, key=lambda flower:flower.color)
        # self.flowers.sort(key=flower.color)
        # for color, flower in sorted_color, self.flowers:
        #     print(f'{flower.name}: {flower.color}')
        return sorted_color


bell = Bell('колокольчик', 10, '5 дней', 'wight', '10 cm')
chamomile = Chamomile('ромашка', 13, '3 дня', 'wight', '12 cm')
peony = Peony('пион', 20, '3 дня', 'red', '30 cm')
gerbera = Gerbera('гербера', 23, '7 дней', 'yellow', '33 cm')

bouquet = Bouquet()
bouquet.add_flower(bell)
bouquet.add_flower(chamomile)
bouquet.add_flower(peony)
bouquet.add_flower(gerbera)

print(bouquet.count_price())
bouquet.average_life()
print(bouquet.sort_by_color())
