import pytest
import requests
from pydantic import BaseModel, Field
from typing import Any
import allure


class ObjData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class NewObjWithData(BaseModel):
    id: str
    name: str
    data: ObjData


class DeletedObject(BaseModel):
    message: str


@allure.feature('Main')
@allure.story('Objects')
@allure.description('Testing creating a new object')
@allure.title('Creating a new object')
@pytest.mark.critical
def test_new_object():
    payload = {
        "name": "Apple MacBook Pro Kate",
        "data": {
            "year": 2025,
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    data = NewObjWithData(**response.json())
    assert response.status_code == 200
    assert data.name == 'Apple MacBook Pro Kate'


@allure.feature('Main')
@allure.story('Objects')
@allure.title('Deleting newly created object')
@pytest.mark.critical
def test_no_more_object(new_object):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object}')
    deleted_data = DeletedObject(**response.json())
    assert response.status_code == 200
    assert deleted_data.message == f'Object with {new_object} been deleted'


@allure.feature('Submain')
@allure.story('Object_ids')
def test_get_by_id(new_object, session_wrap):
    response = requests.get(f'https://api.restful-api.dev/objects/{new_object}')
    assert response.status_code == 200
    assert response.json()['name'] == 'Apple MacBook Pro Kate'


@allure.feature('Submain')
@allure.story('Object_ids')
@allure.severity('Blocker')
@pytest.mark.parametrize(
    'name', ['Apple MacBook 111 Kate', 'Apple MacBook $$$ Kate', 'Apple MacBook Update Kate'],
    ids=['numbers', 'special characters', 'regular']
)
@pytest.mark.critical
def test_change_everyth(new_object, session_wrap, name):
    payload = {
        "name": name,
        "data": {
            "year": 2024,
            "price": 2899,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    with allure.step('Making a request to the API'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{new_object}',
            json=payload
        )
    with allure.step('Checking the name field'):
        assert response.json()['name'] == payload['name']


@allure.feature('Submain')
@allure.story('Minor changes')
@allure.title('Making a single change')
@pytest.mark.smoke
def test_change_someth(new_object, session_wrap):
    payload = {
        "name": "Apple Kate",
        "data": {
            "year": 2023
        }
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_object}',
        json=payload
    )
    assert response.json()['name'] == payload['name']
