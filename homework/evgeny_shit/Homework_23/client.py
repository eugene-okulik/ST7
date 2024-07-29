import os

import allure
import requests
from dotenv import load_dotenv

from homework.evgeny_shit.Homework_23.models import ResponseModel

load_dotenv()

URL = os.getenv('BASE_URL')


def create_payload(name: str, year: int, price: float, cpu_model: str, hard_disk_size: str) -> dict:
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


def validate_response_data(valid_response: ResponseModel, payload: dict):
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


def attach_response(response: requests.Response, name: str):
    allure.attach(response.text, name=name, attachment_type=allure.attachment_type.JSON)


def send_post_request(payload: dict) -> requests.Response:
    return requests.post(URL, json=payload)


def send_get_request(object_id: str) -> requests.Response:
    return requests.get(f"{URL}/{object_id}")


def send_put_request(object_id: str, payload: dict) -> requests.Response:
    return requests.put(f"{URL}/{object_id}", json=payload)


def send_patch_request(object_id: str, payload: dict) -> requests.Response:
    return requests.patch(f"{URL}/{object_id}", json=payload)


def send_delete_request(object_id: str) -> requests.Response:
    return requests.delete(f"{URL}/{object_id}")
