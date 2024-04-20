my_name = input("Как вас зовут? ")
item_to_buy = input("Что вы хотите купить? ")
price = float(input("Сколько это стоит? "))
available_sum = float(input("Сколько у вас есть? "))
savings_per_month = float(input("Сколько можете отложить в месяц? "))

remaining_amount = price - available_sum
months_until_purchase = (remaining_amount / savings_per_month)

print(f"Привет, {my_name}. На покупку {item_to_buy} тебе не хватает {remaining_amount:}")
print("Возможность совершения покупки:", remaining_amount <= 0)
print(f'До покупки осталось {months_until_purchase} месяцев')
