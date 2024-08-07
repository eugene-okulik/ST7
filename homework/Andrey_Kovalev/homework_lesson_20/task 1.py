import requests


def create_object():
    payload = {
        "name": "TOYOTA",
        "data": {
            "year": 2019,
            "price": 1849.99,
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.post('https://api.restful-api.dev/objects',
                             json=payload,
                             headers=headers)

    print(response.json())


def get_object():
    response = requests.get('https://api.restful-api.dev/objects?id=ff8081819127333701912897561003fe')
    print(response.json())


def update_obj():
    payload = {
        "name": "TOYOTA",
        "data": {
            "year": 2019,
            "price": 1849.99,

        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put('https://api.restful-api.dev/objects?id=ff8081819127333701912897561003fe',
                            json=payload,
                            headers=headers
                            )
    print(response.json())


def update_name_object():
    payload = {
        "name": "BMW"

    }
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.patch('https://api.restful-api.dev/objects?id=ff8081819127333701912897561003fe',
                              json=payload, headers=headers)

    assert response.status_code == 200
    print(response.json())


def delete_object():
    response = requests.delete('https://api.restful-api.dev/objects?id=ff8081819127333701912897561003fe')
    print(response.json())
