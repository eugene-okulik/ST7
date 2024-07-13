import allure
import requests

from data.schemas import ObjData, DeleteSingleObject

base_url = 'https://api.restful-api.dev/objects'


class BaseApi:
    response: requests.Response
    response_json: dict
    data: ObjData
    deleted_item_data: DeleteSingleObject

    @allure.step('Check status code')
    def check_status_code_is_(self, code):
        return self.response.status_code == code
