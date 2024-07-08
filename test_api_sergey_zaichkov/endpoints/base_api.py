import allure


class BaseDevice:
    BASE_URL = "https://api.restful-api.dev/objects"
    response = None
    device = None

    @allure.step("Check status code")
    def status_code_is_(self, status_code):
        return self.response.status_code == status_code

    @allure.step("Check response name")
    def response_name_is_(self, name):
        return self.device.name == name

    @allure.step("Check response device ID")
    def response_device_id_is_(self, device_id):
        return self.device.id == device_id
