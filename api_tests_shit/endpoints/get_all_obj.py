import allure
import requests

from api_tests_shit.client import URL, attach_response

from api_tests_shit.endpoints.base_api import BaseApi


class GetAllObject(BaseApi):
    @allure.step('Get all object')
    def get_single_obj(self) -> None:
        self.response = requests.get(URL)
        attach_response(self.response, "Response")
        self.response_json = self.response.json()

    def check_response_is_not_empty(self) -> tuple[bool, str]:
        return len(self.response_json) > 0, f"Expected at least one object, got {len(self.response_json)}"
