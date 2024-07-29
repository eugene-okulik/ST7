import requests
import allure
from test_api_dmitrii.endpoints.base_api import BaseApi
from test_api_dmitrii.tests.data import headers as h
from test_api_dmitrii.tests.data import url


class PutPost(BaseApi):
    @allure.step('Update Post')
    def put_post(self, object_id, payload, header=None):
        headers = header if header else h.headers_temp

        self.response = requests.put(
            f'{url.url}/{object_id}',
            json=payload,
            headers=headers
        )

        self.response_json = self.response.json()
