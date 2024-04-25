import math

name = input("What is your name?\n")
buy = input("What are you going to buy?\n")
price = float(input("How much does it cost?\n"))
current_money = float(input("How much money do you have?\n"))
save_money = float(input("How much can you save per month?\n"))

need_money = max(price - current_money, 0)
make_purchase = current_money >= need_money
months = math.ceil(need_money / save_money)

print(f"Hello, {name}. You don't have enough ${need_money} to buy a {buy}\n"
      f"Possibility of making a purchase: {make_purchase}\n"
      f"{months} months left until purchase")
