import requests

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
    print(response.json())


def get_by_id():
    response = requests.get('https://api.restful-api.dev/objects/ff808181902733350190466878152cfd')
    print(response.json())


def change_everyth():
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
        'https://api.restful-api.dev/objects/ff808181902733350190466878152cfd',
        json=payload
        )
    print(response.json())


def change_someth():
    payload = {
        "name": "Apple Kate",
        "data": {
            "year": 2023
        }
    }
    response = requests.patch(
        'https://api.restful-api.dev/objects/ff808181902733350190466878152cfd',
        json=payload
        )
    print(response.json())


def no_more_object():
    response = requests.delete('https://api.restful-api.dev/objects/ff808181902733350190466878152cfd')
    print(response.json())
