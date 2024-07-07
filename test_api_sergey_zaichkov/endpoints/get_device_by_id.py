import allure
import requests
from test_api_sergey_zaichkov.endpoints.base_api import BaseDevice
from test_api_sergey_zaichkov.models import device_models
from test_api_sergey_zaichkov.tests.data.headers import base_headers


class GetDeviceById(BaseDevice):
    @allure.step("Get device by ID")
    def get_device_by_id(self, device_id, headers=None):
        headers = headers if headers else base_headers
        self.response = requests.get(url=f"{self.BASE_URL}/{device_id}", headers=headers)
        self.device = device_models.GetDevice(**self.response.json())
