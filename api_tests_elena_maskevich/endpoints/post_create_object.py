import requests
import allure
from api_tests_elena_maskevich.endpoints.base_api import BaseApi
from api_tests_elena_maskevich.endpoints.schemas import CreatedObject

base_url = 'https://api.restful-api.dev/objects'

headers_template = {
        'Content-Type': 'application/json',
    }


class PostCreateObj(BaseApi):
    @allure.step('Create object')
    def create_object(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            base_url,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        print(self.response_json)
        self.data = CreatedObject(**self.response_json)

    @allure.step('Check response name')
    def check_response_name(self, name):
        return self.response_json['name'] == name
