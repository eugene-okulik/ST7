"""

Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

"""
import math


def find_hypotenuse(a, b):
    result = math.sqrt(a ** 2 + b ** 2)
    return result


def find_square(a, b):
    result = (a * b) / 2
    return result


print('The result of hypotenuse calculation is', find_hypotenuse(12, 6))
print('The result of square calculation is', find_square(44, 36))
