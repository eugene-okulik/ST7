import datetime

# Обработка даты
date = 'Jan 15, 2023 - 12:05:33'
new_date = datetime.datetime.strptime(date, 'Jan %d, %Y - %H:%M:%f')

print(new_date.strftime('%B'))
print(new_date.strftime('%d.%m.%Y, %H:%M'))

price_list = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

# text = []
# numbers = []
# for item in price_list.splitlines():
# print(item)
# gg = item.split()[0]
# print(gg)
# tt = int(item.split()[1][:-1])
# print(tt)
# text.append(gg)
# numbers.append(tt)

# print(text, numbers)

price_dict = {item.split()[0]: int(item.split()[1][:-1]) for item in price_list.splitlines()}
print()
print(f'List comprehension: {price_dict}, ')
