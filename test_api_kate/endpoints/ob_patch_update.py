import allure
import requests
from test_api_kate.endpoints.base_api import StatusCode


class ObPatchUpdate(StatusCode):
    @allure.step('Making price changes')
    def ob_change_patch(self, ob_id, payload):
        self.response = requests.patch(
            f'https://api.restful-api.dev/objects/{ob_id}',
            json=payload
        )
        self.response_json = self.response.json()

    @allure.step('Checking updated price')
    def ob_price_check(self, price):
        return self.response_json['data']['price'] == price
