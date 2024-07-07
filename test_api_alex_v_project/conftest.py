import pytest
import requests

base_url = 'https://api.restful-api.dev/objects'


@pytest.fixture()
def item_id():
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
        url='https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )

    item_id = response.json()['id']
    yield item_id
    requests.delete(f'{base_url}/{item_id}', headers=headers)
