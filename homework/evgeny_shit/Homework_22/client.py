import os

from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('BASE_URL')


def create_payload(name, year, price, cpu_model, hard_disk_size):
    data = {
        "year": year,
        "price": price,
        "CPU model": cpu_model,
        "Hard disk size": hard_disk_size,
    }
    return {
        "name": name,
        "data": data
    }


def validate_response_data(valid_response, payload):
    assert valid_response.name == payload['name'], \
        f"Expected name {payload['name']}, got {valid_response.name}"
    assert valid_response.data.year == payload['data']['year'], \
        f"Expected year {payload['data']['year']}, got {valid_response.data.year}"
    assert valid_response.data.price == payload['data']['price'], \
        f"Expected price {payload['data']['price']}, got {valid_response.data.price}"
    assert valid_response.data.cpu_model == payload['data']['CPU model'], \
        f"Expected CPU model {payload['data']['CPU model']}, got {valid_response.data.cpu_model}"
    assert valid_response.data.hard_disk_size == payload['data']['Hard disk size'], \
        f"Expected Hard disk size {payload['data']['Hard disk size']}, got {valid_response.data.hard_disk_size}"
