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
def create_device_endpoint():
    return CreateDevice()


@pytest.fixture()
def new_device(create_device_endpoint, get_device_by_id_endpoint, delete_device_endpoint):
    # Creating device
    create_device_endpoint.create_device(payload=payloads.create_device)

    assert create_device_endpoint.status_code_is_(200)
    device_id = create_device_endpoint.device.id

    yield device_id

    get_device_by_id_endpoint.get_device_by_id(device_id)
    if get_device_by_id_endpoint.status_code_is_(200):
        # Deleting device
        delete_device_endpoint.delete_device(device_id)
        assert delete_device_endpoint.status_code_is_(200)


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
