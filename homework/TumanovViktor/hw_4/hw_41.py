user_name = input('Как вас зовут ? ')
us_count = input('Что вы хотите купить ? ')
us_price = int(input('Сколько это стоит ? '))
how_many = int(input('Сколько у вас есть ? '))
how_otlohit = int(input('Сколько можете отложить в месяц? '))
sum_ot = us_price - how_many
print('Привет ' + user_name + '.', 'На покупку ' + us_count, 'тебе не хватает ', sum_ot)
suma = how_many >= us_price
mount = (us_price - how_many) / how_otlohit
print('Возможность совершения покупки: ', suma)
print('покупки осталось ', mount, 'месяцев')
