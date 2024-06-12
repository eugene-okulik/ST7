class Bouquet:
    def __init__(self):
        self.flowers = []  # list of flower objects

    def add_flower(self, flower):  # bouquet creation - adding single flower to a bouquet
        self.flowers.append(flower)

    @property
    def bouquet_total_price(self):
        total_sum = sum(flower.price for flower in self.flowers)
        return total_sum

    @property
    def get_lifespan(self):
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_by_lifetime(self):
        self.flowers.sort(key=lambda flower: flower.lifespan)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def sort_by_length(self):
        self.flowers.sort(key=lambda flower: flower.stem_length)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_flowers(self, key):  # nice universal method
        self.flowers.sort(key=lambda flower: getattr(flower, key))
