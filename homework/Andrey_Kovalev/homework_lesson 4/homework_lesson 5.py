name = input("Как вас зовут? ")
item = input("Что вы хотите купить? ")
price = float(input("Сколько это стоит? "))
available_funds = float(input("Сколько у вас есть? "))
savings_per_month = float(input("Сколько можете отложить в месяц? "))

remaining_price = price - available_funds
can_purchase = remaining_price <= savings_per_month * 200

print(f"Привет, {name}. На покупку {item} тебе не хватает {remaining_price}")
print("Возможность совершения покупки:", can_purchase)

remaining_months = remaining_price / savings_per_month
print("До покупки осталось", int(remaining_months), "месяцев")

