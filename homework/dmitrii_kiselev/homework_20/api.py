import requests


def create_object():

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

    return response.json()


def get_object_by_id(o_id):

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(
        f'https://api.restful-api.dev/objects/{o_id}',
        headers=headers
    )

    assert response.status_code == 200

    return response.json()


def update_object(o_id):

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
        f'https://api.restful-api.dev/objects/{o_id}',
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    return response.json()


def partually_update_object(o_id):

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
        f'https://api.restful-api.dev/objects/{o_id}',
        json=payload,
        headers=headers
    )

    assert response.status_code == 200

    return response.json()


def delete_object(o_id):

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.delete(
        f'https://api.restful-api.dev/objects/{o_id}',
        headers=headers
    )

    assert response.status_code == 200

    return response.json(), response


object_id = create_object()['id']
print(create_object())
print(get_object_by_id(object_id))
print(update_object(object_id))
print(get_object_by_id(object_id))
print(partually_update_object(object_id))
print(get_object_by_id(object_id))
print(delete_object(object_id))
print(get_object_by_id(object_id))
