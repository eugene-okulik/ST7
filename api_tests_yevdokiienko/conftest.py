import pytest
import requests
from api_tests_yevdokiienko.tests.data import payloads
from api_tests_yevdokiienko.endpoints.post_objects import PostObjects
from api_tests_yevdokiienko.endpoints.get_by_id import GetById
from api_tests_yevdokiienko.endpoints.put_object import UpdatePut
from api_tests_yevdokiienko.endpoints.patch_object import PatchObject
from api_tests_yevdokiienko.endpoints.delete_object import DeleteObject


url = 'https://api.restful-api.dev/objects'


@pytest.fixture(scope='session')
def session_info():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def get_object_id(create_object_endpoint):
    create_object_endpoint.create_object(payloads.new_object)
    object_id = create_object_endpoint.response_json['id']
    yield object_id
    requests.delete(f'{url}/{object_id}')


@pytest.fixture()
def delete_object(request):
    request.object_id = None
    yield request
    print(f'I will delete object with id {request.object_id}')


@pytest.fixture()
def create_object_endpoint():
    return PostObjects()


@pytest.fixture()
def get_object_endpoint():
    return GetById()


@pytest.fixture()
def put_object_endpoint():
    return UpdatePut()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
