import requests
import allure
from api_tests_elena_maskevich.endpoints.base_api import BaseApi

base_url = 'https://api.restful-api.dev/objects'


class PatchOjb(BaseApi):
    @allure.step('Patch object')
    def patch_object(self, payload, object_id):
        self.response = requests.patch(
            url=f"{base_url}/{object_id}",
            json=payload,
        )
        print(self.response)
        self.response_json = self.response.json()
        print(self.response_json)
