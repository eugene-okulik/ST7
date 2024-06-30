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


@pytest.fixture()
def before_after_greetings():
    print('Start testing')
    yield
    print('Testing completed')


def test_get_single_item(item_id, before_after_greetings):
    response = requests.get(f'{base_url}/{item_id}')
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_all():
    response = requests.get(f'{base_url}')
    assert response.status_code == 200


def test_update_item(item_id):
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
    requests.put(
        base_url,
        json=payload,
        headers=headers
    )

    assert payload['data']['color'] == 'silver'


@pytest.mark.regression
def test_delete(item_id):
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.delete(f'{base_url}/{item_id}',
                               headers=headers)
    assert response.status_code == 200, 'Opps!?! publication vanishing has not been done yet'
