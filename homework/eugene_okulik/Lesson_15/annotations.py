from typing import Literal, List


def make_dict(value):
    return {value: value}


def calc(x: int, y: int) -> dict:
    result = x * y
    return make_dict(result)


calc(3, 5)
calc('sdf', 'sdf')

calc_result = calc(4, 7)
# print(calc_result.)


class Flower:
    def __init__(self, price, color):
        self.price = price
        self.color = color


def show_flower_price(cvetok: Flower):
    print(cvetok.price)


rose = Flower(12, 'white')
tulip = Flower(5, 'Black')

xxx = 'hi!'


def hi_or_bye(word: Literal['hi', 'by']):
    # if word == 'hi':
    #     print('Hello')
    # elif word == 'bye':
    #     print('Good bye')
    # else:
    #     print('give me hi or bye')
    match word:
        case ['hi', 'by']:
            print('Hello')
        case 'bye':
            print('Good bye')
        case _:
            print('give me hi or bye')


hi_or_bye('hi')


def sum_all(list_of_int: List[int]):
    return sum(list_of_int)


sum_all(['sdf', 'sdfsdf'])
sum_all([9, 9])
