import allure
import requests
from api_tests_eokulik.enpoints.schemas import Publication


class BaseApi:
    response: requests.Response
    response_json: dict
    data: Publication

    @allure.step('Check status code')
    def check_status_code_is_(self, code):
        return self.response.status_code == code
