import random
import string
from faker import Faker

fake = Faker()


class UserData:
    @staticmethod
    def generate_firstname():
        return fake.first_name()

    @staticmethod
    def generate_lastname():
        return fake.last_name()

    @staticmethod
    def generate_email():
        email = f"{fake.first_name().lower()}.{fake.last_name().lower()}{random.randint(1, 1000)}@example.com"
        return email

    @staticmethod
    def generate_password(length=10):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password
