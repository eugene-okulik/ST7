import requests
import allure
from api_tests_tumanov.endpoints.base_api import BaseApi


class GetId(BaseApi):
    @allure.step('Get obj')
    def get_obj_id(self, new_obj):
        self.response = requests.request('GET', f'{self.url}/{new_obj}')
        self.response_json = self.response.json()
