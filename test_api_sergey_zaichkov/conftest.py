import pytest
import requests
from test_api_sergey_zaichkov.endpoints.create_device import CreateDevice
from test_api_sergey_zaichkov.endpoints.get_device_by_id import GetDeviceById
from test_api_sergey_zaichkov.tests.data import payloads
from test_api_sergey_zaichkov.endpoints.put_device import PutDevice
from test_api_sergey_zaichkov.endpoints.patch_device import PatchDevice
from test_api_sergey_zaichkov.endpoints.delete_device import DeleteDevice


@pytest.fixture(scope='session', autouse=True)
def start_completed():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def new_device():
    url = "https://api.restful-api.dev/objects"

    response = requests.post(url=url, json=payloads.create_device)
    assert response.status_code == 200, "Status code is not 200"
    device_id = response.json().get('id')
    yield device_id

    if requests.get(f"{url}/{device_id}").status_code == 200:
        response = requests.delete(url=f"{url}/{device_id}")
        assert response.status_code == 200, "Status code is not 200"


@pytest.fixture()
def create_device_endpoint():
    return CreateDevice()


@pytest.fixture()
def get_device_by_id_endpoint():
    return GetDeviceById()


@pytest.fixture()
def put_device_endpoint():
    return PutDevice()


@pytest.fixture()
def patch_device_endpoint():
    return PatchDevice()


@pytest.fixture()
def delete_device_endpoint():
    return DeleteDevice()
