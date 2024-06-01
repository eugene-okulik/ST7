PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

new_list = {item: int(price[:-1]) for item, price in [x.split() for x in PRICE_LIST.split('\n')]}
print(new_list)
