import pytest
import requests
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
def get_object_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        url,
        json=payload,
        headers=headers
    )
    object_id = response.json()['id']
    yield object_id
    requests.delete(f'{url}/{object_id}')


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
