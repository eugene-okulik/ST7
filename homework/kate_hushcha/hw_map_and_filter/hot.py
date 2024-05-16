
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29,
                25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_temp = list(filter(lambda y: y > 28, temperatures))
max_temp = max(hot_temp)
min_temp = min(hot_temp)
average_temp = sum(hot_temp) / len(hot_temp)

print(max_temp)
print(min_temp)
print(round(average_temp))
