import pytest
import requests
import allure

url = 'https://api.restful-api.dev/objects'


@pytest.fixture(scope='session')
def session_info():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def get_object_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        url,
        json=payload,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'{url}/{object_id}')
