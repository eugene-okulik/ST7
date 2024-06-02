class Bouquet:
    def __init__(self):
        self.flowers = []  # list of flower objects

    def add_flower(self, flower):  # bouquet creation
        self.flowers.append(flower)

    def bouquet_total_price(self):
        total_sum = sum(flower.price for flower in self.flowers)
        return total_sum
