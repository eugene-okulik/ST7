import pytest
import requests


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
    # print(f'Created publication {response.json()["id"]}')
    yield object_id
    requests.delete(f'{url}/{object_id}')
    # print(f'Deleted {object_id}')


def test_create_object_post(get_object_id, session_info):
    print(session_info)
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
    assert response.status_code == 200
    # print("Object created successfully!")


def test_get_object_by_id(get_object_id, session_info):
    print(session_info)
    response = requests.get(f'{url}/{get_object_id}')
    assert response.status_code == 200
    # print("Object retrieved successfully!")
    # print(response.json())


@pytest.mark.smoke
def test_update_object_put(get_object_id, session_info):
    print(session_info)
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }
    response = requests.put(
        f'{url}/{get_object_id}',
        json=payload
    )
    assert response.status_code == 200
    # print("Object updated successfully!")
    # print(response.json())


@pytest.mark.critical
def test_partially_update_object_patch(get_object_id, session_info):
    print(session_info)
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(
        f'{url}/{get_object_id}',
        json=payload
    )
    assert response.status_code == 200
    # print("Name updated successfully!")
    assert response.json()['name'] == payload['name']
    # print(response.json())


def test_delete_object(get_object_id, session_info):
    # print(session_info)
    response = requests.delete(f'{url}/{get_object_id}')
    assert response.status_code == 200
    # print("Deleted successfully!")
