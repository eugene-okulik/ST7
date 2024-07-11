import allure
import requests
from test_api_kate.endpoints.base_api import StatusCode


class ObById(StatusCode):
    @allure.step('Check the object by ID')
    def get_ob_by_id(self, ob_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{ob_id}')
        self.response_json = self.response.json()
