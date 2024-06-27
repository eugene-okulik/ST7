import requests
import pytest


@pytest.fixture()
def create_object():
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
def follow_the_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.mark.regression
def test_create_object(follow_the_testing):

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

    assert response.status_code == 200


@pytest.mark.regression
@pytest.mark.smoke
def test_get_object(create_object):
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(
        f'https://api.restful-api.dev/objects/{create_object}',
        headers=headers
    )

    assert response.status_code == 200
    print('id = ', create_object)


@pytest.mark.regression
@pytest.mark.critical
def test_update_object(create_object):

    payload = {
        "name": "Asus Ultrabook 2a",
        "data": {
            "year": 2022,
            "price": 899.99,
            "CPU model": "Intel Core i3",
            "Hard disk size": "128 Mb"
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.put(
        f'https://api.restful-api.dev/objects/{create_object}',
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()['name'] == payload["name"]
    print('id = ', create_object)


@pytest.mark.regression
def test_partually_update_object(create_object):

    payload = {
        "data": {
            "Hard disk size": "256 Mb",
            "price": 1837.99,
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.patch(
        f'https://api.restful-api.dev/objects/{create_object}',
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()['data']['Hard disk size'] == payload['data']['Hard disk size']
    assert response.json()['data']['price'] == payload['data']['price']
    print('id = ', create_object)
