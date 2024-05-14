# С помощью функции map или filter создайте из этого списка новый список с жаркими днями. Будем считать жарким всё, что выше 28.

# Распечатайте из нового списка самую высокую температуру самую низкую и среднюю.

temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]


# def hot_day(temp):
#     return temp > 28

# hot_days_list = list(filter(hot_day,temperatures))

hot_days_list = list(filter(lambda x: x > 28, temperatures))
print(hot_days_list)
print(f'Максимальное значение -{max(hot_days_list)}')
print(f'Минимальное значение - {min(hot_days_list)}')
print(f'Среднее значение -{round(sum(hot_days_list)/len(hot_days_list), 2)}')
