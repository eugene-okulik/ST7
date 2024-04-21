import math

name = input('как вас зовут?\n')
target = input('что вы хотите купить?\n')
price = float(input('сколько это стоит?\n'))
availability = float(input('сколько у вас есть?\n'))
opportunities = float(input('сколько можете отложить в месяц?\n'))

print(f'Привет, {name}. На покупку {target} тебе не хватает {price - availability} \n'
      f'Возможность совершения покупки: {availability >= price} \n'
      f'До покупки осталось {int(math.ceil((price - availability) / opportunities))} месяцев')
