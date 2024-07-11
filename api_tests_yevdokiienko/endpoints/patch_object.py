import allure
import requests
from api_tests_yevdokiienko.endpoints.base_api import BaseApi
from api_tests_yevdokiienko.tests.data.url import url


class PatchObject(BaseApi):
    @allure.step('Partially update object')
    def update_object(self, get_object_id, payload):
        self.response = requests.patch(
            url=f'{url}/{get_object_id}',
            json=payload,
        )
        self.response_json = self.response.json()
