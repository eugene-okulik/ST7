import allure
import requests
from test_api_sergey_zaichkov.endpoints.base_api import BaseDevice
from test_api_sergey_zaichkov.models import device_models
from test_api_sergey_zaichkov.tests.data.headers import base_headers


class CreateDevice(BaseDevice):
    @allure.step("Create device")
    def create_device(self, payload, headers=None):
        headers = headers if headers else base_headers
        self.response = requests.post(url=self.BASE_URL, json=payload, headers=headers)
        self.device = device_models.Device(**self.response.json())
