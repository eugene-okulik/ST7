import allure
import requests
from api_tests_yevdokiienko.endpoints.schemas import NewObjectData, DeleteObjData


class BaseApi:
    response: requests.Response
    response_json: dict
    data: NewObjectData
    data_deleted: DeleteObjData

    @allure.step('Check status code')
    def check_status_code_is_(self, code):
        return self.response.status_code == code

    @allure.step('Check response name')
    def check_response_name_is_(self, name):
        return self.response_json['name'] == name

    @allure.step('Check response year')
    def check_response_year_is_(self, year):
        return self.response_json['data']['year'] == year

    @allure.step('Check response color')
    def check_response_color_is_(self, color):
        return self.response_json['data']['color'] == color

    @allure.step('Check response price')
    def check_response_price_is_(self, price):
        return self.response_json['data']['price'] == price
