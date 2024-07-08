import allure
import requests
from api_tests_tumanov.endpoints.base_api import BaseApi


class PostPosts(BaseApi):
    @allure.step('Create Obj')
    def create_object(self, payload, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.post(
            f'{self.url}',
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
        print(self.response.json())

        return self.response
