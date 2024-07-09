import allure
import requests


class BaseApi():
    response = requests.Response
    response_json = dict

    @allure.step('Check status code')
    def check_status_code_is_200(self, code):
        return self.response.status_code == code
