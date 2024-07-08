import pytest
import allure
from test_api_sergey_zaichkov.tests.data import payloads
from test_api_sergey_zaichkov.tests.data import headers


@allure.feature('Device')
class TestDeviceApi:
    # ADDING
    @allure.story('Adding')
    def test_add_device(self, create_device_endpoint):
        create_device_endpoint.create_device(
            payload=payloads.create_device,
            headers=headers.base_headers
        )

        assert create_device_endpoint.status_code_is_(200)
        assert create_device_endpoint.response_name_is_(payloads.create_device.get('name'))

    # GETTING
    @allure.description("This test gets device by id")
    @allure.story('Getting')
    def test_get_device_by_id(self, new_device, get_device_by_id_endpoint):
        get_device_by_id_endpoint.get_device_by_id(device_id=new_device)

        assert get_device_by_id_endpoint.status_code_is_(200)
        assert get_device_by_id_endpoint.response_name_is_(payloads.create_device.get('name'))
        assert get_device_by_id_endpoint.response_device_id_is_(new_device)

    # PUTTING
    @pytest.mark.parametrize('payload', payloads.put_devices)
    @allure.story('Changing')
    def test_change_device_put(self, put_device_endpoint, new_device, payload):
        put_device_endpoint.put_device(device_id=new_device, payload=payload)

        assert put_device_endpoint.status_code_is_(200)
        assert put_device_endpoint.response_device_id_is_(new_device)
        assert put_device_endpoint.response_name_is_(payload.get('name'))

    # PATCHING
    @allure.story('Changing')
    def test_change_device_patch(self, patch_device_endpoint, new_device):
        patch_device_endpoint.patch_device(new_device, payload=payloads.patch_device)

        assert patch_device_endpoint.status_code_is_(200)
        assert patch_device_endpoint.response_name_is_(payloads.patch_device.get('name'))

    # DELETING
    @allure.story('Deleting')
    def test_delete_device(self, delete_device_endpoint, new_device):
        delete_device_endpoint.delete_device(device_id=new_device)

        assert delete_device_endpoint.status_code_is_(200)
        assert delete_device_endpoint.check_del_message("has been deleted"), "Del message isn't correct"

    @allure.story('Deleting')
    # @pytest.mark.skip
    def test_delete_non_existent_device(self, delete_device_endpoint):
        delete_device_endpoint.delete_device(device_id=999)

        assert delete_device_endpoint.status_code_is_(404), "Status code is not 404"
        assert delete_device_endpoint.check_del_message("id = 999 doesn't exist"), "Del message isn't correct"
