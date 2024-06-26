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


@pytest.mark.smoke
def test_get_by_id(new_object, session_wrap):
    response = requests.get(f'https://api.restful-api.dev/objects/{new_object}')
    assert response.status_code == 200
    assert response.json()['name'] == 'Apple MacBook Pro Kate'


@pytest.mark.critical
def test_change_everyth(new_object, session_wrap):
    payload = {
        "name": "Apple MacBook Update Kate",
        "data": {
            "year": 2024,
            "price": 2899,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{new_object}',
        json=payload
    )
    assert response.json()['name'] == payload['name']


@pytest.mark.smoke
def test_change_someth(new_object, session_wrap):
    payload = {
        "name": "Apple Kate",
        "data": {
            "year": 2023
        }
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_object}',
        json=payload
    )
    assert response.json()['name'] == payload['name']
