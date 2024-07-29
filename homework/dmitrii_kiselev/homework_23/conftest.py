import requests
import pytest


@pytest.fixture()
def object_id():
    print('Start testing')
    payload = {
        "name": "Asus Ultrabook 2",
        "data": {
            "year": 2021,
            "price": 837.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
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

    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    print('Testing completed')


@pytest.fixture()
def follow_the_testing_without_object():
    print('Start testing')
    yield
    print('Testing completed')
