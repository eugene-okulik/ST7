temperatures = [20, -15, 32, 34, -21, 0]

new_list = list(map(lambda x: (str(x) + '° тепла') if x > 0 else (str(x) + '° холода') if x < 0 else 'На улице ноль',
                    temperatures))

print(new_list)
