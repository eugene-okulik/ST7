import allure
import requests
from api_tests_yevdokiienko.endpoints.base_api import BaseApi
from api_tests_yevdokiienko.tests.data.url import url
from api_tests_yevdokiienko.tests.data.headers import headers_template


class PostObjects(BaseApi):
    @allure.step('Create object')
    def create_object(self, payload, header=None):
        headers = header if header else headers_template
        self.response = requests.post(
            url,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        self.object_id = self.response_json['id']
