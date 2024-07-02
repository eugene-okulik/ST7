import pytest
import requests


@pytest.fixture()
def new_object():
    payload = {
        "name": "Apple MacBook Pro Kate",
        "data": {
            "year": 2025,
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    new_object_id = response.json()["id"]
    print(f'Created object {response.json()["id"]}')
    yield new_object_id
    requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    print(f'Deleted object {new_object_id}')


@pytest.fixture(scope='session')
def session_wrap():
    print("Start Testing")
    yield
    print("End Testing")
