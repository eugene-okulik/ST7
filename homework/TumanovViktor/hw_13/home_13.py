class Flowrs:
    def __init__(self, name, color, svezhest, lifespan, price, srok_zhizni):
        self.name = name
        self.color = color
        self.svezhest = svezhest
        self.lifespan = lifespan
        self.price = price
        self.srok_zhizni = srok_zhizni


class Pion(Flowrs):
    def __init__(self, name, color, svezhest, lifespan, price, srok_zhizni):
        super().__init__(name, color, svezhest, lifespan, price, srok_zhizni)


class Tulpan(Flowrs):
    def __init__(self, name, color, svezhest, lifespan, price, srok_zhizni):
        super().__init__(name, color, svezhest, lifespan, price, srok_zhizni)


class Buket:
    def __init__(self):
        self.tsvety = []

    def add_flower(self, tsvetok):
        self.tsvety.append(tsvetok)

    def lifespan(self):
        lifespan = sum(tsvetok.srok_zhizni for tsvetok in self.tsvety)
        return lifespan / len(self.tsvety) if len(self.tsvety) > 0 else 0

    def sort(self, key):
        self.tsvety.sort(key=lambda x: getattr(x, key))

    def search(self, key, value):
        return [tsvetok for tsvetok in self.tsvety if getattr(tsvetok, key) == value]


roza = Flowrs("Роза", "Красный", 77, 24, 150, 10)
arhideya = Flowrs("Архидея", "Фиолетовый", 88, 20, 80, 7)
romashka = Flowrs("Ромашка", "Белый с жёлтый", 99, 12, 55, 6)
fialki = Flowrs("Фиалки", "Синий", 450, 756, 255, 15)
pion = Flowrs("Пион", "Бордовый", 100, 20, 200, 25)
tulpan = Flowrs("Тюльпан", "Жёлтый", 90, 10, 100, 15)


buket = Buket()
buket.add_flower(roza)
buket.add_flower(arhideya)
buket.add_flower(romashka)
buket.add_flower(fialki)
buket.add_flower(pion)
buket.add_flower(tulpan)


print("Среднее время увядания букета:", int(buket.lifespan()))
buket.sort("price")
print("Цветы в букете отсортированы по цене:", [tsvetok.name for tsvetok in buket.tsvety])
yellow_color = buket.search("color", "Жёлтый")
print("Цветы в букете желтого цвета:", [tsvetok.name for tsvetok in yellow_color])
