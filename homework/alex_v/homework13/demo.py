from abstract_flower import Flower
from homework.alex_v.homework13.bouquet import Bouquet
from homework.alex_v.homework13.buttercup import Buttercup
from homework.alex_v.homework13.chamomile import Chamomile
from homework.alex_v.homework13.rose import Rose
from homework.alex_v.homework13.tulip import Tulip


class Demo:
    rose = Rose('red', 5, 7, 50)
    tulip = Tulip('yellow', 3, 5, 40)
    buttercup = Buttercup('white', 8, 4, 35)
    chamomile = Chamomile("blue", 7, 7, 25)

    my_bouquet = Bouquet()
    my_bouquet.add_flower(rose)
    my_bouquet.add_flower(tulip)
    my_bouquet.add_flower(buttercup)
    my_bouquet.add_flower(chamomile)

    print(f'Total bouquet price is : {my_bouquet.bouquet_total_price}')
    print(f'Average bouquet life is : {my_bouquet.get_lifespan} days')

    my_bouquet.sort_by_lifetime()

    for flower in my_bouquet.flowers:
        print(f"{flower.name}: {flower.lifespan} days")

    my_bouquet.sort_by_price()
    for flower in my_bouquet.flowers:
        print(f"{flower.name}: {flower.price} euro")
