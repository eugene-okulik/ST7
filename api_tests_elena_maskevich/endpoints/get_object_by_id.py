import allure
import requests
from api_tests_elena_maskevich.endpoints.base_api import BaseApi

base_url = 'https://api.restful-api.dev/objects'


class GetObjectById(BaseApi):

    @allure.step('GetObject')
    def get_object(self, id):
        self.response = requests.request('GET', f'{base_url}/{id}')
        self.response_json = self.response.json()
