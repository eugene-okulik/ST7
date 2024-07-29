import allure
import requests
from test_api_kate.endpoints.ob_schema import NewObjWithData


class StatusCode():
    response: requests.Response
    response_json: dict
    data: NewObjWithData

    @allure.step('Check status code')
    def check_status_code_is_(self, code):
        return self.response.status_code == code
