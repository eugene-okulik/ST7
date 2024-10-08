import pytest
import requests


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


@pytest.mark.critical
def test_new_obj():
    payload = {
        "name": "NarateL",
        "data": {
            "year": 30,
            "price": "100$",
            "CPU model": "World 2024",
            "Hard disk size": "8880 TB"
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
    print(f'Обьект успешно создан {response.json()["id"]}')


@pytest.fixture()
def session_info():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.mark.critical
def test_update_obj(new_obj, session_info):
    payload = {
        "name": "NarateL",
        "data": {
            "year": 1223,
            "price": "77770$",
            "CPU model": "World 2024",
            "Hard disk size": "1000 TB",
            "color": "Green"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{new_obj}',
                            json=payload
                            )
    assert response.status_code == 200


@pytest.mark.smoke
def test_change_obj(new_obj, session_info):
    payload = {
        "name": "NarateL",
        "data": {
            "year": 10,
            "price": "5000$"
        }
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_obj}',
        json=payload
    )
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']


@pytest.mark.smoke
def test_get_id(new_obj, session_info):
    response = requests.request('GET', f'https://api.restful-api.dev/objects/{new_obj}')
    assert response.json()['name'] == 'NarateL'
    assert response.status_code == 200
    assert response.json()['id'] == new_obj


def test_delete_obj(new_obj, session_info):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_obj}')
    assert response.status_code == 200
