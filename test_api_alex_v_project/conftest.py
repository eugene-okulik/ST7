import pytest
import requests
from test_api_alex_v_project.endpoints.get_item import GetById
from test_api_alex_v_project.endpoints.delete_item import DeleteItem
from test_api_alex_v_project.endpoints.patch_item import PatchItem
from test_api_alex_v_project.endpoints.post_item import PostItem
from test_api_alex_v_project.endpoints.put_item import PutItem

base_url = 'https://api.restful-api.dev/objects'


@pytest.fixture()
def item_id_fixture():
    payload = {
        "name": "Horizont AI Edition 2000",
        "data": {
            "year": 1980,
            "price": 500,
            "CPU model": "Intel Core i7",
            "Hard disk size": "250 GB"
        }

    }
    headers = {
        'Content-Type': 'application/json',
    }
    response = requests.post(
        url='https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )

    item_id = response.json()['id']
    yield item_id
    requests.delete(f'{base_url}/{item_id}', headers=headers)


@pytest.fixture()
def get_item_endpoint():
    return GetById()


@pytest.fixture()
def post_item_endpoint():
    return PostItem()


@pytest.fixture()
def patch_item_endpoint():
    return PatchItem()


@pytest.fixture()
def put_item_endpoint():
    return PutItem()


@pytest.fixture()
def delete_item_endpoint():
    return DeleteItem()
