# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

# не совсем понятна формулировка задания. Что значит "даны" и "получить". Сделал через инпут и принт...

leg1, leg2 = int(input()), int(input())

hypotenuse = (leg1 ** 2 + leg2 ** 2) ** 0.5
square = (leg1 * leg2) / 2

print(hypotenuse)
print(square)
