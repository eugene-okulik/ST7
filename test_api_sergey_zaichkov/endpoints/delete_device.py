import allure
import requests
from test_api_sergey_zaichkov.endpoints.base_api import BaseDevice
from test_api_sergey_zaichkov.models import device_models
from test_api_sergey_zaichkov.tests.data.headers import base_headers


class DeleteDevice(BaseDevice):
    del_device_message = None

    @allure.step("Delete device by ID")
    def delete_device(self, device_id, headers=None):
        headers = headers if headers else base_headers
        self.response = requests.delete(url=f"{self.BASE_URL}/{device_id}")
        if self.response.status_code == 200:
            self.del_device_message = device_models.DelDevice(**self.response.json()).message
        else:
            self.del_device_message = device_models.DelNotExistDevice(**self.response.json()).error

    @allure.step("Check delete message")
    def check_del_message(self, message):
        return message in self.del_device_message
