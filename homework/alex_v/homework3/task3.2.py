"""

Даны числа x и y. Получить x − y / 1 + xy

"""


def find_calculation_result(x, y):
    result = (x - y) / (1 + x * y)
    return result


print('The result of calculation is ', find_calculation_result(5, 9))
