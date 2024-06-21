import requests


def create_obj():
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
    print(response.json())


def search_id():
    response = requests.get('https://api.restful-api.dev/objects?id=ff80818190273335019039fb10002268')
    print(response.json())


def update_obj():
    payload = {
        "name": "NarateL",
        "data": {
            "year": 30,
            "price": "100$",
            "CPU model": "World 2024",
            "Hard disk size": "1000 TB",
            "color": "Red"

        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.put('https://api.restful-api.dev/objects/ff80818190273335019039fb10002268',
                            json=payload,
                            headers=headers
                            )
    print(response.json())


def update_obj2():
    payload = {
        "name": "Naro-Fran"
    }
    response = requests.patch(
        'https://api.restful-api.dev/objects/ff80818190273335019039fb10002268',
        json=payload
        )
    assert response.status_code == 200
    print(response.json())


def delete():
    response = requests.delete('https://api.restful-api.dev/objects/ff80818190273335019039fb10002268')
    print(response.json())
