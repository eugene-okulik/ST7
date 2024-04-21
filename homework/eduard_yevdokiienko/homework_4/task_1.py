# Напишите программу, которая спрашивает:
# Как вас зовут?
# Что вы хотите купить?
# Сколько это стоит?
# Сколько у вас есть?
# Сколько можете отложить в месяц?
# В результате программа должна распечатать, например, такое:
# Привет, Петя. На покупку Ferrari тебе не хватает 1000000
# Возможность совершения покупки: False
# До покупки осталось 200 месяцев

name = input('What is your name?\n')
print('Hello', name)
item = input('What do you want to buy?\n')
print(item, ', nice')
price = int(input('What is the price? '))
print('So, great')
money_currently = int(input('How much do you currently have? '))
print(f'Yes, {money_currently}, not enough')
money_savings = int(input('How much you can save in a month? '))

money_lack = price - money_currently
month_to_save = (price - money_currently) // money_savings

print(f'So let me to help you, {name}.You need {money_lack} to buy a {item}')
print('Possibility of making a purchase: ', money_currently == price)
print(f'Left until purchase {month_to_save} month')
print('Good luck')
