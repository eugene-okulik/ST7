import pytest
import requests
import allure
from test_api_alex_v_project.endpoints.base_api import BaseApi, base_url

class PatchItem(BaseApi):
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
