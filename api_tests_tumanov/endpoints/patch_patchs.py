import allure
import requests
from api_tests_tumanov.endpoints.base_api import BaseApi


class PatchPatch(BaseApi):
    @allure.step('Cheng Object')
    def patch_change_obj(self, new_obj, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            f'{self.url}/{new_obj}',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        print(self.response.json())

        return self.response

    @allure.step('Check price')
    def check_correct_(self, key, value):
        return self.response_json['data'][key] == value
