import allure
import requests
from api_tests_yevdokiienko.endpoints.base_api import BaseApi
from api_tests_yevdokiienko.tests.data.url import url


class UpdatePut(BaseApi):
    @allure.step('Put object')
    def put_object(self, get_object_id, payload):
        self.response = requests.put(
            f'{url}/{get_object_id}',
            json=payload
        )
        self.response_json = self.response.json()
