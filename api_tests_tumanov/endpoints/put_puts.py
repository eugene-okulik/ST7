import allure
import requests
from api_tests_tumanov.endpoints.base_api import BaseApi


class PutPuts(BaseApi):
    @allure.step('Update Object')
    def put_update(self, new_obj, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            f'{self.url}/{new_obj}',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        print(self.response.json())

        return self.response
