class Flower:
    def __init__(self, name, color, length, cost, lifespan):
        self.name = name
        self.color = color
        self.length = length
        self.cost = cost
        self.lifespan = lifespan


class Rose(Flower):
    def __init__(self, color, length, cost, lifespan):
        super().__init__('Rose', color, length, cost, lifespan)


class Tulip(Flower):
    def __init__(self, color, length, cost, lifespan):
        super().__init__('Tulip', color, length, cost, lifespan)


class Lily(Flower):
    def __init__(self, color, length, cost, lifespan):
        super().__init__('Lily', color, length, cost, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)
        print(
            f"Added flower: {flower.name} ({flower.color}), cost: {flower.cost} rub, "
            + f"length: {flower.length} sm, lifetime: {flower.lifespan} days")

    def get_cost(self):
        total_cost = sum(flower.cost for flower in self.flowers)
        print(f"Bouquet cost: {total_cost} rub")
        return total_cost

    def get_avg_lifespan(self):
        if not self.flowers:
            avg_lifespan = 0
        else:
            avg_lifespan = sum(flower.lifespan for flower in self.flowers) / len(self.flowers)
        print(f"Average life time of a bouquet: {avg_lifespan} days")
        return avg_lifespan

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))
        print(f"Flowers in a bouquet after sorting by {key}:")
        for flower in self.flowers:
            print(f"{flower.name} ({flower.color}): {getattr(flower, key)}")

    def find_flowers(self, **kwargs):
        results = self.flowers
        found_flowers = f"Found flowers by parameters {kwargs}:"
        for key, value in kwargs.items():
            results = [flower for flower in results if getattr(flower, key) == value]
        if results:
            print(found_flowers)
            for flower in results:
                print(f"{flower.name} ({flower.color}), cost: {flower.cost} rub, length: {flower.length} sm, "
                      + f"lifetime: {flower.lifespan} days")
        else:
            print(found_flowers)
            print("Nothing found")
        return results


rose = Rose(color='red', length=40, cost=200, lifespan=7)
tulip = Tulip(color='yellow', length=30, cost=90, lifespan=5)
lily = Lily(color='white', length=50, cost=350, lifespan=10)
lily2 = Lily(color='black', length=50, cost=420, lifespan=10)

bouquet = Bouquet()
bouquet.add_flower(rose)
bouquet.add_flower(tulip)
bouquet.add_flower(lily)
bouquet.add_flower(lily2)

# Get statistics
bouquet.get_cost()
bouquet.get_avg_lifespan()

# Sort by cost
bouquet.sort_flowers('cost')

# Search flowers by color
bouquet.find_flowers(lifespan=10)
bouquet.find_flowers(lifespan=11)
bouquet.find_flowers(lifespan=5)
