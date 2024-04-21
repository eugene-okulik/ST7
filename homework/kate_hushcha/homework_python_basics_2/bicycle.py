
user_name = input('What is your name?\n')
gift = input('What do you want to buy?\n')
price = int(input('How much does it cost?\n'))
initial_money = int(input('How much do you have right now?\n'))
monthly_input = int(input('What is going to be your monthly input?\n'))

money_needed = price - initial_money
months_needed = (price - initial_money) / monthly_input
months_needed = int(months_needed)
possibility_now = price is initial_money

print('Hello,', user_name) 
print('To buy a', gift, 'you need $', money_needed)
print('Possibility to buy it right now:', possibility_now)
print('You will get your', gift, 'in', months_needed, 'months')