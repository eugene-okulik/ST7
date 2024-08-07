import pytest
import requests
from pydantic import BaseModel, Field

base_url = 'https://api.restful-api.dev/objects'


@pytest.mark.parametrize('name',
                         ['SONY ERICSSON',
                          '12345',
                          '!@#$%^&'])
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
