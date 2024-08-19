import pytest
import requests
import allure
from test_api_alex_v_project.endpoints.base_api import BaseApi, base_url


class PatchItem(BaseApi):
    @allure.step("Partial change of an item")
    def partial_update_item(self, payload, item_id):
        self.response = requests.patch(
            url=f"{base_url}/{item_id}",
            json=payload
        )
        self.response_json = self.response.json()
