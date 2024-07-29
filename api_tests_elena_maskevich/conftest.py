import requests
import pytest
from api_tests_elena_maskevich.endpoints.get_object_by_id import GetObjectById
from api_tests_elena_maskevich.endpoints.post_create_object import PostCreateObj
from api_tests_elena_maskevich.endpoints.update_put_object import PutOjb
from api_tests_elena_maskevich.endpoints.update_patch_object import PatchOjb
from api_tests_elena_maskevich.endpoints.delete_object import DeleteOjb

base_url = 'https://api.restful-api.dev/objects'


@pytest.fixture()
def object_id():
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
        'Content-Type': 'application/json',
    }

    response = requests.post(
        base_url,
        json=payload,
        headers=headers
    )
    obj_id = response.json()['id']
    print(f'Created object id {response.json()["id"]}')
    yield obj_id
    requests.delete(f'{base_url}/{obj_id}')
    print(f'Deleted object id {obj_id}')


@pytest.fixture()
def get_object_id():
    return GetObjectById()


@pytest.fixture()
def create_object_id():
    return PostCreateObj()


@pytest.fixture()
def put_object_id():
    return PutOjb()


@pytest.fixture()
def patch_object_id():
    return PatchOjb()


@pytest.fixture()
def deleted_object_id():
    return DeleteOjb()
