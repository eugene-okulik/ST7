# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

import math


leg1 = 8
leg2 = 6
hypotenuse = math.sqrt(leg1 ** 2 + leg2 ** 2)
area = (leg1 * leg2) / 2

print(hypotenuse, area)
