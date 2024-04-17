# import math

first_cathetus = 35
second_cathetus = 15

hypotenuse = (first_cathetus ** 2 + second_cathetus ** 2) ** 0.5
# hypotenuse_math = round(math.sqrt(first_cathetus ** 2 + second_cathetus ** 2), 3)

area = 0.5 * first_cathetus * second_cathetus

print(f"Hypotenuse = {hypotenuse:.2f}")
print(f"Area = {area:.2f}")
# print(f"Hypotenuse = {hypotenuse_math}")
