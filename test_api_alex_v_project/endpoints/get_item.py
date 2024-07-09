import requests
import allure
from test_api_alex_v_project.endpoints.base_api import BaseApi

base_url = 'https://api.restful-api.dev/objects'


class GetById(BaseApi):

    @allure.step('Get item by unique Id')
    def get_item_by_id(self, item_id):
        self.response = requests.get(f'{base_url}/{item_id}')
        self.response_json = self.response.json()
