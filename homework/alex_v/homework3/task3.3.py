"""

Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

"""
import math


def find_average(a, b):
    result = (a + b) / 2
    return result


def find_geometric_mean(a, b):
    result = math.sqrt(a * b)
    return result


print('The result of average is', find_average(67, 13))
print('The result of geometric mean is', find_average(123, 44))
