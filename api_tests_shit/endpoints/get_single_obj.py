import allure
import requests

from api_tests_shit.client import URL, attach_response
from api_tests_shit.endpoints.base_api import BaseApi


class GetObject(BaseApi):
    @allure.step('Get object')
    def get_single_obj(self, object_id) -> None:
        self.response = requests.get(f"{URL}/{object_id}")
        attach_response(self.response, "Response")
        self.response_json = self.response.json()

    @allure.step('Check response id')
    def check_response_id_is_(self, object_id) -> tuple[bool, str]:
        return self.response_json['id'] == object_id, f"Expected id {object_id}, got {self.response_json['id']}"
