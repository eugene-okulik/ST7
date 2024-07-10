import requests
import allure
from test_api_alex_v_project.endpoints.base_api import BaseApi, base_url
from test_api_alex_v_project.tests.data.schemas import DeleteSingleObject


class DeleteItem(BaseApi):
    @allure.step('Delete item by id')
    def delete_item_by_id(self, item_id):
        self.response = requests.delete(f'{base_url}/{item_id}')
        self.response_json = self.response.json()
        self.deleted_item_data = DeleteSingleObject(**self.response_json)
