import requests
import allure
from test_api_kate.endpoints.base_api import StatusCode

headers_template = {
    'Content-Type': 'application/json',
}

class PostObjects(StatusCode):
    @allure.step('Create new object')
    def create_object(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            'https://api.restful-api.dev/objects',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()

    @allure.step('Check object name')
    def object_name_is_(self, name):
        return self.response_json['name'] == name
