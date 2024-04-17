# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

import math


x = 8
y = 2
arithmetic_mean = (x + y) / 2
geometric_mean = math.sqrt(x * y)
geometric_mean2 = (x * y) ** (1 / 2)

print(arithmetic_mean, geometric_mean, geometric_mean2)
