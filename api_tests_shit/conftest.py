import pytest
import requests

from api_tests_shit.client import URL
from api_tests_shit.tests.data import payloads
from api_tests_shit.endpoints.put_upd_obj import PutUpdObj
from api_tests_shit.endpoints.get_single_obj import GetObject
from api_tests_shit.endpoints.get_all_obj import GetAllObject
from api_tests_shit.endpoints.post_add_obj import PostAddObj
from api_tests_shit.endpoints.delete_del_obj import DeleteObj
from api_tests_shit.endpoints.patch_part_upd_obj import PatchPartUpdObj


@pytest.fixture(scope='session')
def session_info() -> None:
    print('Start testing', end=' ')
    yield
    print(' Testing completed')


@pytest.fixture
def object_id() -> str:
    payload = payloads.create_obj
    response = requests.post(URL, json=payload)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f"{URL}/{obj_id}")


@pytest.fixture
def object_id_without_del() -> str:
    payload = payloads.create_obj
    response = requests.post(URL, json=payload)
    obj_id = response.json()['id']
    return obj_id


@pytest.fixture
def get_obj_endpoint():
    return GetObject()


@pytest.fixture
def get_all_obj_endpoint():
    return GetAllObject()


@pytest.fixture
def create_obj_endpoint():
    return PostAddObj()


@pytest.fixture
def update_obj_endpoint():
    return PutUpdObj()


@pytest.fixture
def partial_update_obj_endpoint():
    return PatchPartUpdObj()


@pytest.fixture
def delete_obj_endpoint():
    return DeleteObj()
