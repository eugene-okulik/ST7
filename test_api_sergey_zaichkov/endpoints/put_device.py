import allure
import requests
from test_api_sergey_zaichkov.endpoints.base_api import BaseDevice
from test_api_sergey_zaichkov.models import device_models
from test_api_sergey_zaichkov.tests.data.headers import base_headers


class PutDevice(BaseDevice):
    @allure.step("Put device by ID")
    def put_device(self, device_id, payload, headers=None):
        headers = headers if headers else base_headers
        self.response = requests.put(
            url=f"{self.BASE_URL}/{device_id}",
            json=payload,
            headers=headers
        )
        self.device = device_models.PutDevice(**self.response.json())
