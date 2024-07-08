import pytest
import requests
import allure
from api_tests_tumanov.endpoints.get_id import GetId
from api_tests_tumanov.endpoints.delete_obj import DeleteObj
from api_tests_tumanov.endpoints.post_posts import PostPosts
from api_tests_tumanov.endpoints.put_puts import PutPuts
from api_tests_tumanov.endpoints.patch_patchs import PatchPatch


@allure.feature('Fixture')
@pytest.fixture()
def new_obj():
    payload = {
        "name": "NarateL",
        "data": {
            "year": 30,
            "price": "100$",
            "CPU model": "World 2024",
            "Hard disk size": "1000 TB"
        }
    }
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload
    )
    new_obj_id = response.json()['id']
    print(f'Создание объекта {new_obj_id}')
    yield new_obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{new_obj_id}')
    print(f'Удаление объекта {new_obj_id}')


@pytest.fixture()
def get_obj_endpoint():
    return GetId()


@pytest.fixture()
def create_obj_endpoint():
    return PostPosts()


@pytest.fixture()
def put_update_endpoint():
    return PutPuts()


@pytest.fixture()
def patch_change_endpoint():
    return PatchPatch()


@pytest.fixture()
def delete_obj_endpoint():
    return DeleteObj()
