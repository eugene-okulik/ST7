first_name = input('Mr. ''Как вас зовут ? ')
product = input('Что вы хотите купить ? ')
price = int(input('Сколько это стоит ? '))
cash = int(input('Сколько у вас есть ? '))
savings_cash_per_month = int(input('Сколько можете отложить в месяц? '))


sum_m: int = price - cash


print('Привет ' + first_name + '.', 'На покупку ' + product, 'тебе не хватает ', sum_m)
summ = cash >= price
mount = (price - cash) / savings_cash_per_month
print('Возможность совершения покупки: ', summ)
print('покупки осталось ', mount, 'месяцев')
