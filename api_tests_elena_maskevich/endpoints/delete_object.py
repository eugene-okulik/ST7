import requests
import allure
from api_tests_elena_maskevich.endpoints.base_api import BaseApi
from api_tests_elena_maskevich.endpoints.schemas import DeletedObject

base_url = 'https://api.restful-api.dev/objects'


class DeleteOjb(BaseApi):
    @allure.step('Delete object')
    def delete_object(self, object_id):
        self.response = requests.delete(
            url=f"{base_url}/{object_id}",
        )
        print(self.response)
        self.response_json = self.response.json()
        print(self.response_json)
        self.data_deleted = DeletedObject(**self.response_json)
