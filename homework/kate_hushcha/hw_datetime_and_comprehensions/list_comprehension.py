
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''


new_list = PRICE_LIST.split('\n')
kate_dict = {tag[0]: int(tag[1][:-1]) for tag in [item.split() for item in new_list]}

print(kate_dict)
