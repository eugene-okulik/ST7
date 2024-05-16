temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25,
                29, 29, 31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = list(filter(lambda temp: temp > 28, temperatures))

max_temp = max(hot_days)
min_temp = min(hot_days)
mean_temp = sum(hot_days) / len(hot_days)

print(f"Max temperature is {max_temp}\n"
      f"Min temperature is {min_temp}\n"
      f"Mean temperature is {mean_temp}\n")
