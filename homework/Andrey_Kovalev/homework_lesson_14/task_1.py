from datetime import datetime


def get_user_age_in_days():
    while True:
        try:
            user_input = input("Введите вашу дату рождения в формате ГГГГ-ММ-ДД: ")

            birth_date = datetime.strptime(user_input, "%Y-%m-%d")

            current_date = datetime.now()

            age_in_days = (current_date - birth_date).days

            print(f"Ваш возраст: {age_in_days} дней.")
            break
        except ValueError:
            print("Некорректный формат даты. Пожалуйста, введите дату в формате ГГГГ-ММ-ДД.")


get_user_age_in_days()
