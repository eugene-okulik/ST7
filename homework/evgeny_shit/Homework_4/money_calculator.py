name = input("What's your name? ")
item = input("What you want to buy? ")
cost = float(input("How much does it cost? "))
current_money = float(input("How much do you have? "))
monthly_savings_text = "How much you can set aside per month? "
monthly_savings = float(input(monthly_savings_text))

money_needed = max(cost - current_money, 0)
purchase_possible = money_needed == 0
months_needed = int((money_needed // monthly_savings) + (money_needed % monthly_savings > 0))

print('_' * len(monthly_savings_text))
print(f"\nHi, {name}. \nFor the purchase of {item} you don't have enough {money_needed}")
print(f"Possibility of making a purchase: {purchase_possible}")
print(f"We're one purchase away {months_needed} months")
