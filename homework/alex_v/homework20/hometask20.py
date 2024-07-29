import requests

base_url = 'https://api.restful-api.dev/objects'


def create_object():
    payload = {
        "name": "Horizont AI Edition 2000",
        "data": {
            "year": 1980,
            "price": 500,
            "CPU model": "Intel Core i7",
            "Hard disk size": "250 GB"
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

    response.json()
    assert response.status_code == 200
    return response.json()


def find_object_by(obj_id):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.get(f'{base_url}/{obj_id}',
                            headers=headers)
    assert response.status_code == 200
    print(response.json())
    return response.json()


def adjust_object(obj_id):
    payload = {
        "name": "Horizont AI Edition 2000",
        "data": {
            "year": 1980,
            "price": 1999,
            "CPU model": "Intel Core i7",
            "Hard disk size": "250 GB",
            "color": "silver"
        }

    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.put(
        base_url,
        json=payload,
        headers=headers
    )
    return response.json()


def partial_object_adjustment(obj_id):
    payload = {
        "data": {
            "price": 3900,
            "Hard disk size": "400 GB",
            "color": "green"
        }

    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.patch(
        base_url,
        json=payload,
        headers=headers
    )
    assert response.status_code == 200
    return response.json()


def delete_object(obj_id):
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.delete(f'{base_url}/{obj_id}',
                               headers=headers)
    assert response.status_code == 200
    return response.json(), response


obj_id = create_object()['id']
find_object_by(obj_id)
adjust_object(obj_id)
partial_object_adjustment(obj_id)
delete_object(obj_id)
find_object_by(obj_id)
