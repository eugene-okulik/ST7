import allure
import requests

from api_tests_shit.client import URL, validate_response

from api_tests_shit.endpoints.base_api import BaseApi

from api_tests_shit.endpoints.schemas import ResponseSchema


class PatchPartUpdObj(BaseApi):
    @allure.step('Update part of object')
    def part_update_object(self, payload, object_id) -> None:
        self.response = requests.patch(f"{URL}/{object_id}", json=payload)
        response_json = self.response.json()

        validate_response(self, response_json, "Response", ResponseSchema)
