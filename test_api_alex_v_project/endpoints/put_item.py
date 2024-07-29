import requests
import allure
from test_api_alex_v_project.endpoints.base_api import BaseApi, base_url


class PutItem(BaseApi):
    @allure.step("Set new data for an item")
    def update_item(self, item_id, payload):
        self.response = requests.put(
            url=f"{base_url}/{item_id}",
            json=payload
        )
        self.response_json = self.response.json()
