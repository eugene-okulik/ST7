# Даны два числа. Найти среднее арифметическое и среднее геометрическое этих чисел

# не совсем понятна формулировка задания. Что значит "даны" и "получить". Сделал через инпут и принт...

x, y = int(input()), int(input())

arithmetic_mean = (x + y) / 2
geometric_mean = (x * y) ** 0.5

print(arithmetic_mean)
print(geometric_mean)
