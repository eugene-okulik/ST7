import pytest
import requests


@pytest.fixture()
def publication_id():
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
    pub_id = response.json()['id']
    print(f'Создание публикации {pub_id}')
    yield pub_id
    requests.delete(f'https://api.restful-api.dev/objects/{pub_id}')
    print(f'Удаление publication {pub_id}')


@pytest.fixture()
def session_info():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.mark.critical
def test_update_obj(publication_id, session_info):
    payload = {
        "name": "NarateL",
        "data": {
            "year": 1223,
            "price": "77770$",
            "CPU model": "World 2024",
            "Hard disk size": "1000 TB",
            "color": "Red"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{publication_id}',
                            json=payload,
                            )
    assert response.status_code == 200
    print('Update', response.json())


def test_patch_jbj(publication_id, session_info):
    payload = {
        "name": "NarateL",
        "data": {
            "year": 10,
            "price": "500000$"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.patch(
        f'https://api.restful-api.dev/objects/{publication_id}',
        json=payload,
        headers=headers
    )
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_all(publication_id, session_info):
    response = requests.request('GET', f'https://api.restful-api.dev/objects/{publication_id}')
    assert response.status_code == 200
