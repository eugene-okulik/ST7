import allure
import requests

from api_tests_shit.client import URL, validate_response

from api_tests_shit.endpoints.base_api import BaseApi

from api_tests_shit.endpoints.schemas import DeleteResponseSchema


class DeleteObj(BaseApi):
    @allure.step('Delete object')
    def delete_object(self, object_id) -> None:
        self.delete_response = requests.delete(f"{URL}/{object_id}")
        delete_response = self.delete_response.json()

        validate_response(self, delete_response, "Delete Response", DeleteResponseSchema)
