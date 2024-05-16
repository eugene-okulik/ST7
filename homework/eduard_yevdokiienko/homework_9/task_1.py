# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё,
# что выше 28.
# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.


temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29,
                + 31, 33, 31, 30, 32, 30, 28, 24, 23]


def sort(x):
    return x >= 28


hot_temp_list = list(filter(sort, temperatures))
print(hot_temp_list)

max_temp = max(hot_temp_list)
min_temp = min(hot_temp_list)
mid_temp = sum(hot_temp_list) / len(hot_temp_list)

print(max_temp, min_temp, mid_temp)
