import allure
import requests


class BaseApi:
    response_json = None
    response = None
    headers = {'Content-Type': 'application/json'}
    url = 'https://api.restful-api.dev/objects'

    @allure.step('Check staus code')
    def check_status_code_is_(self, code):
        assert self.response.status_code == code

    @allure.step('Check response name')
    def check_response_name_is_(self, name):
        assert self.response_json['name'] == name
