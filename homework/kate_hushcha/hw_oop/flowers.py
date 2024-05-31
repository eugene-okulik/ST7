
class Flowers:
    f_type = 'plants'
    florets = True

    def __init__(self, name, color, life_time, size, price):
        self.name = name
        self.color = color
        self.life_time = life_time
        self.size = size
        self.price = price


    def bloom_time(self):
        pass


class OutdoorFlowers(Flowers):
    water = False
    grow_start = 'Spring'
    stem_size = 45


    def __init__(self, name, color, life_time, size, price, insects):
        super().__init__(name, color, life_time, size, price)
        self.insects = insects


    def bloom_time(self):
        print('Summer')


class IndoorFlowers(Flowers):
    water = True
    grow_start = 'Year around'
    stem_size = 20

    def bloom_time(self):
        print('Spring and Summer')


daffodils = OutdoorFlowers('Daffodil', 'Yellow', 20, 'medium', 10, 'bumblebees')
crocuses = OutdoorFlowers('Crocus', 'Violet', 10, 'small', 5, 'bees')
kalanchoe = IndoorFlowers('Kalanchoe', 'White', 30, 'big', 17 )
cactus = IndoorFlowers('Cactus', 'Green', 40, 'small', 9)


class Bouquet():
    def __init__(self):
        self.flowers = []


    def b_flowers(self, flower):
        self.flowers.append(flower)
        print(f'Bouquet flowers: {flower.name}')


    def f_price(self):
        self.price = sum(flower.price for flower in self.flowers)
        print(f'Bouquet price is {self.price}')

    
    def fade_time(self):
        self.fade_time = sum(flower.life_time for flower in self.flowers) / 4
        print(f'Bouquet fading time is {round(self.fade_time)} days')


    def sort_flowers(self):
        self.flowers.sort(key=lambda flower : flower.stem_size)
        print(f'Flower are sorted:')
        for flower in self.flowers:
            print(f' - {flower.name} with stem size {flower.stem_size}')


    def find_flowers(self, color):
        for flower in self.flowers:
            if flower.color == color:
                print(f'{flower.color} is {flower.name}')


bouquet = Bouquet()
bouquet.b_flowers(daffodils)
bouquet.b_flowers(crocuses)
bouquet.b_flowers(kalanchoe)
bouquet.b_flowers(cactus)

bouquet.f_price()
bouquet.fade_time()
bouquet.sort_flowers()
bouquet.find_flowers('Yellow')
