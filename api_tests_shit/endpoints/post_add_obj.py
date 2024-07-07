import allure
import requests

from api_tests_shit.client import URL, validate_response

from api_tests_shit.endpoints.base_api import BaseApi

from api_tests_shit.endpoints.schemas import ResponseSchema, DeleteResponseSchema


class PostAddObj(BaseApi):
    @allure.step('Add object')
    def create_object(self, payload) -> None:
        self.response = requests.post(URL, json=payload)
        response_json = self.response.json()
        valid_response = validate_response(self, response_json, "Response", ResponseSchema)

        obj_id: str = valid_response.id

        self.delete_response = requests.delete(f"{URL}/{obj_id}")
        delete_response = self.delete_response.json()

        validate_response(self, delete_response, "Delete Response", DeleteResponseSchema)
