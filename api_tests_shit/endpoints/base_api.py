import allure
import requests

from api_tests_shit.endpoints.schemas import ResponseSchema, DeleteResponseSchema


class BaseApi:
    obj_id: str
    response_json: dict
    response: requests.Response
    valid_response: ResponseSchema
    delete_response: requests.Response
    valid_delete_response: DeleteResponseSchema

    @allure.step('Check status code')
    def check_status_code(self, response: requests.Response, status_code: int) -> tuple[bool, str]:
        return response.status_code == status_code, (f"Expected status code {status_code}, "
                                                     + f"got {response.status_code}")

    @allure.step('Check response name')
    def check_response_name_is_(self, name: str) -> tuple[bool, str]:
        return self.valid_response.name == name, (f"Expected name {name}, "
                                                  + f"got {self.valid_response.name}")

    @allure.step('Check response year')
    def check_response_year_is_(self, year: int) -> tuple[bool, str]:
        return self.valid_response.data.year == year, (f"Expected year {year}, "
                                                       + f"got {self.valid_response.data.year}")

    @allure.step('Check response price')
    def check_response_price_is_(self, price: float) -> tuple[bool, str]:
        return self.valid_response.data.price == price, (f"Expected price {price}, "
                                                         + f"got {self.valid_response.data.price}")

    @allure.step('Check response cpu model')
    def check_response_cpu_model_is_(self, cpu_model: str) -> tuple[bool, str]:
        return self.valid_response.data.cpu_model == cpu_model, (f"Expected cpu model {cpu_model}, "
                                                                 + f"got {self.valid_response.data.cpu_model}")

    @allure.step('Check response hard disk size')
    def check_response_hard_disk_size_is_(self, hard_disk: str) -> tuple[bool, str]:
        return self.valid_response.data.hard_disk == hard_disk, (f"Expected hard disk size {hard_disk}, "
                                                                 + f"got {self.valid_response.data.hard_disk}")

    @allure.step('Check response message')
    def check_response_message_is_(self, message: str) -> tuple[bool, str]:
        return message in self.valid_delete_response.message, (f"Expected message to contain '{message}', "
                                                               + f"got {self.valid_delete_response.message}")
