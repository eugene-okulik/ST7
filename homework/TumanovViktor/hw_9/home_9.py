temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

jar_temp = list(filter(lambda x: x >= 28, temperatures))
max_temp = max(jar_temp)
min_temp = min(jar_temp)
average = sum(jar_temp) / len(jar_temp)

print('Жаркие дни', jar_temp, '\n' 'Минимальная температура', min_temp, '\n' 'Максимальная температура', max_temp,
      '\n', round(average))
