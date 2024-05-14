temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

max_temp = list(filter(lambda x: x == max(temperatures), temperatures))
min_temp = list(filter(lambda x: x == min(temperatures), temperatures))
jar_temp = list(filter(lambda x: x >= 28, temperatures))
average = sum(temperatures) / len(temperatures)
print('максимальная температура', list(set(max_temp)),
      '\n' 'минимальная температура', min_temp,
      '\n' 'Жаркие дни', jar_temp,
      '\n', round(average))
