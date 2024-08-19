import requests
import allure
import json
from api_tests_eokulik.enpoints.base_api import BaseApi
from api_tests_eokulik.enpoints.schemas import Publication


class GetById(BaseApi):
    @allure.step('Get publication')
    def get_publication(self, pub_id):
        self.response = requests.request('GET', f'https://jsonplaceholder.typicode.com/posts/{pub_id}')
        try:
            # self.response_json = self.response.json()
            self.data = Publication(**self.response.json())
            # self.data = Publication(**self.response_json)
        except json.JSONDecodeError:
            pass
