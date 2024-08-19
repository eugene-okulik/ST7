import requests
import allure
from test_api_dmitrii.endpoints.base_api import BaseApi
from test_api_dmitrii.tests.data import headers as h
from test_api_dmitrii.tests.data import url


class PostPost(BaseApi):
    @allure.step('Create Post')
    def create_object(self, payload, header=None):
        headers = header if header else h.headers_temp

        self.response = requests.post(
            url.url,
            json=payload,
            headers=headers
        )

        self.response_json = self.response.json()
