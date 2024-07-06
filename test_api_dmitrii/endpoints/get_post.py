import requests
import allure
from test_api_dmitrii.endpoints.base_api import BaseApi
from test_api_dmitrii.tests.data import url


class GetPost(BaseApi):
    @allure.step('Get created Post')
    def get_post(self, object_id):

        self.response = requests.get(
            f'{url.url}/{object_id}'
        )

        self.response_json = self.response.json()
