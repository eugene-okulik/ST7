import pytest
import requests
import allure

base_url = 'https://api.restful-api.dev/objects'


@pytest.mark.parametrize('name',
                         ['SONY ERICSSON',
                          '12345',
                          '!@#$%^&'])
@allure.feature('Advanced check')
@allure.description('Changing of the item')
def test_update_item(item_id, name):
    payload = {
        "name": name,
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


@pytest.mark.skip(reason='blocked bug #327')
@allure.feature('Advanced check')
@allure.description('Partial changing of the item')
@pytest.mark.parametrize('price', ['-5', '0', '', '2.99'])
def test_partial_update_item(item_id, price):
    payload = {
        "data": {
            "year": 1980,
            "price": price,
            "CPU model": "Intel Core i7",
            "Hard disk size": "250 GB",
            "color": "silver"
        }

    }
    headers = {
        'Content-Type': 'application/json',
    }
    requests.patch(
        base_url,
        json=payload,
        headers=headers
    )

    assert payload['data']['color'] == 'silver'
