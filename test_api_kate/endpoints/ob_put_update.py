import allure
import requests
from test_api_kate.endpoints.base_api import StatusCode


class ObPutUpdate(StatusCode):
    @allure.step('Making changes to the object')
    def ob_change_put(self, ob_id, payload):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{ob_id}', json=payload)
        self.response_json = self.response.json()

    @allure.step('Checking updated name')
    def ob_updated_name(self, name):
        return self.response_json['name'] == name
