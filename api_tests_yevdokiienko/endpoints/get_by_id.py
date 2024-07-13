import allure
import requests
from api_tests_yevdokiienko.endpoints.base_api import BaseApi
from api_tests_yevdokiienko.tests.data.url import url


class GetById(BaseApi):

    @allure.step('Get object')
    def get_object(self, get_object_id):
        self.response = requests.get(f'{url}/{get_object_id}')
        self.response_json = self.response.json()
