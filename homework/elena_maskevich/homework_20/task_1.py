# Для тестирования возьмем небольшое тестовое API: https://restful-api.dev
# Нужно написать код, который взамодействует с перечисленными в спецификации функции этого API, а именно:
# Создание объекта
# Получение объекта по его id
# Изменение объекта с помощью метода PUT
# Изменение объекта с помощью метода PATCH
# Удаление объекта
# Выполняйте всё задание так же, как я делал на занятии, - каждый запрос в отдельной функции.

import requests

base_url = 'https://api.restful-api.dev/objects'


def create_object():
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
    response_created_object = response.json()
    assert response.status_code == 200
    print(response_created_object)
    obj_id = response_created_object.get('id')
    return obj_id


def get_by_id(obj_id):
    response = requests.get(f'{base_url}/{obj_id}')
    assert response.status_code == 200, 'Incorrect status code'
    print(response.json())


def update_with_put(obj_id):
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
        f'{base_url}/{obj_id}',
        json=payload
    )

    assert response.status_code == 200, 'Incorrect status code'
    print(response.json())


def change_object_patch(obj_id):
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(
        url=f"{base_url}/{obj_id}",
        json=payload
    )
    assert response.status_code == 200, "Status code is not 200"
    print(response.json())


def delete_object(obj_id):
    response = requests.delete(f'{base_url}/{obj_id}')
    assert response.status_code == 200, "Status code is not 200"
    print('Successfully deleted')


obj_id = create_object()
get_by_id(obj_id)
update_with_put(obj_id)
change_object_patch(obj_id)
delete_object(obj_id)
