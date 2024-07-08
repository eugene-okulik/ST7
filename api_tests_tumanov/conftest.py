import pytest
import requests
import allure


@allure.feature('Fixture')
@pytest.fixture()
def new_obj():
    payload = {
        "name": "NarateL",
        "data": {
            "year": 30,
            "price": "100$",
            "CPU model": "World 2024",
            "Hard disk size": "1000 TB"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    new_obj_id = response.json()['id']
    print(f'Создание объекта {new_obj_id}')
    yield new_obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{new_obj_id}')
    print(f'Удаление объекта {new_obj_id}')