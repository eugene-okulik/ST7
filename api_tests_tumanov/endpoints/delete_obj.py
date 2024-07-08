import requests
import allure
from api_tests_tumanov.endpoints.base_api import BaseApi


class DeleteObj(BaseApi):
    @allure.step('check delete obj')
    def delete_obj(self, new_obj):
        self.response = requests.delete(
            f'https://api.restful-api.dev/objects/{new_obj}'
        )
        self.response_json = self.response.json()
        return self.response
