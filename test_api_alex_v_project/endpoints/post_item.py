import requests
import allure
from test_api_alex_v_project.endpoints.base_api import BaseApi

headers_template = {
    'Content-Type': 'application/json',
}


class PostItem(BaseApi):
    @allure.step('Create item')
    def create_item(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            url='https://api.restful-api.dev/objects',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()

    @allure.step('Check item title')
    def check_response_title_is_(self, name):
        return self.response.json()['name'] == name
