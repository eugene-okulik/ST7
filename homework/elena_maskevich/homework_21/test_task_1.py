# Оформите тесты из задания 20 как тесты, которые можно запустить с помощью Pytest.
# Сделайте так, чтобы перед запуском всех тестов распечатывалось "Start testing", а по завершении всех тестов
# - "Testing completed"
# Тесты на изменение, получение по id и удаление объекта сделайте независимыми. Т.е. сделайте так, чтобы перед запуском
# каждого из этих тестов запускалось выполнение предусловия - создание объекта для этого теста, а после теста, пусть
# созданный объект удаляется.
# Пометьте один тест как smoke, а один как critical и сделайте так, чтобы при запуске автотестов не было никаких
# ворнингов.

import requests
import random
import pytest

base_url = 'https://api.restful-api.dev/objects'


@pytest.fixture(scope='session')
def session_info():
    print('Start testing')
    yield random.randrange(100, 200)
    print('Testing completed')


@pytest.fixture()
def object_id():
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
        'Content-Type': 'application/json',
    }

    response = requests.post(
        base_url,
        json=payload,
        headers=headers
    )
    obj_id = response.json()['id']
    print(obj_id)
    print(f'Created object id {response.json()["id"]}')
    yield obj_id
    requests.delete(f'{base_url}/{obj_id}')
    print(f'Deleted object id {obj_id}')


@pytest.mark.smoke
def test_get_by_id(object_id, session_info):
    response = requests.get(f'{base_url}/{object_id}')
    assert response.status_code == 200, 'Incorrect status code'
    print(f'Object with id {object_id}')


@pytest.mark.critical
def test_update_with_put(object_id, session_info):
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
        f'{base_url}/{object_id}',
        json=payload
    )

    assert response.status_code == 200, 'Incorrect status code'
    print(f'Updated put object with id {object_id}')


def test_change_object_patch(object_id, session_info):
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(
        url=f"{base_url}/{object_id}",
        json=payload
    )
    assert response.status_code == 200, "Status code is not 200"
    print(f'Updated patch object with id {object_id}')
