import allure
import requests
from test_api_kate.endpoints.base_api import StatusCode
from test_api_kate.endpoints.ob_schema import DeletedObject


class ObDeleted(StatusCode):
    @allure.step('Deleting object')
    def ob_deleted(self, ob_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{ob_id}')
        self.response_json = DeletedObject(**self.response.json())
