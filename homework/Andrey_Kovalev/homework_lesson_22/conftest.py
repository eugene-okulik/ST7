import pytest
import requests


@pytest.fixture()
def new_obj():
    payload = {
        "name": "TOYOTA",
        "data": {
            "year": 2019,
            "price": 1849.99
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


@pytest.fixture()
def session_info():
    print("Start testing")
    yield
    print("Testing completed")
