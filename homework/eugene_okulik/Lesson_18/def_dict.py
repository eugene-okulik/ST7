import collections

with open('shops.txt') as shops_file:
    shops = shops_file.read()

shops_list = shops.splitlines()
print(shops_list)

shops_dict = collections.defaultdict(list)
for line in shops_list:
    categ, shop = line.split(':')
    # if not shop in shops_dict:
    #     shops_dict[shop] = [categ]
    # else:
    shops_dict[shop].append(categ)


print(shops_dict)

# {'Минск': ['маг1', 'молоко'], 'Москва': ['спорт'], 'Брест': ['хлеб','товары']}
