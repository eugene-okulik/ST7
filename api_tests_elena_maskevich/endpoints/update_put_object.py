import requests
import allure
from api_tests_elena_maskevich.endpoints.base_api import BaseApi

base_url = 'https://api.restful-api.dev/objects'


class PutOjb(BaseApi):
    @allure.step('Put object')
    def put_object(self, object_id, payload):
        self.response = requests.put(
            url=f"{base_url}/{object_id}",
            json=payload
        )
        self.response_json = self.response.json()
        print(self.response_json)
