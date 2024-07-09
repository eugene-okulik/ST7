import allure
import requests
from api_tests_elena_maskevich.endpoints.schemas import CreatedObject, DeletedObject


class BaseApi:
    response: requests.Response
    response_json: dict
    data: CreatedObject
    data_deleted: DeletedObject

    @allure.step('Check status code')
    def check_status_code_(self, code):
        return self.response.status_code == code
