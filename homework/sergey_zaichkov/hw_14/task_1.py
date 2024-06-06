import datetime

now = datetime.datetime.now()

while True:
    input_birthday = input("Type your birthday: ")
    try:
        birthday = datetime.datetime.strptime(input_birthday, "%d.%m.%Y")
        how_many_days = (now - birthday).days
        print(f"You have already lived {how_many_days} days")
    except ValueError:
        print("Correct format is Day.Month.Year")
    else:
        break
