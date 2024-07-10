import requests
import allure
from test_api_alex_v_project.tests.data import headers
from test_api_alex_v_project.endpoints.base_api import BaseApi, base_url


class PutItem(BaseApi):
    @allure.step("Adjust item")
    def update_item(self, payload):
        self.response = requests.put(
            url=base_url,
            json=payload,
            headers=headers
        )
        self.response_json = self.response.json()
