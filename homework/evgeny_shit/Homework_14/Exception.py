from datetime import datetime


def calculate_age_in_days(birth_date):
    today = datetime.today()
    age_in_days = (today - birth_date).days
    return age_in_days


def main():
    while True:
        birth_date_input = input("Enter your date of birth in the format DD-MM-YYYY: ")
        try:
            birth_date = datetime.strptime(birth_date_input, '%d-%m-%Y')
            age_in_days = calculate_age_in_days(birth_date)
            age_in_years = age_in_days / 365.25  # Taking leap years into account

            if age_in_years < 3 / 12:
                print(f"You're {age_in_days} days old? Please enter your correct date of birth.")
            elif age_in_years < 3:
                age_in_months = age_in_days / 30.4375  # Average number of days in a month
                print(f"You're {int(age_in_months)} months old? Please enter your correct date of birth.")
            elif age_in_years > 100:
                print(f"You're {int(age_in_years)} years old? Please enter your correct date of birth.")
            else:
                print(f"Your age in days: {age_in_days}")
                break
        except ValueError:
            print("Incorrect date format. Please use the format DD-MM-YYYY.")


if __name__ == "__main__":
    main()
