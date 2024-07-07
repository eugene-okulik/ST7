import pytest
import requests
from pydantic import BaseModel, Field
import allure

base_url = 'https://api.restful-api.dev/objects'


class ObjData(BaseModel):
    year: int
    price: int
    cpu_value: str = Field(alias='CPU model')
    disk_size: str = Field(alias='Hard disk size')


class NewObjWithData(BaseModel):
    name: str
    data: ObjData


@pytest.mark.regression
@allure.description('Creation of the item')
@allure.feature('Basic check')
@allure.story('Create')
def test_create_item(item_id, before_after_greetings):
    payload = {
        "name": "Horizont Extreme Edition",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(
        base_url,
        json=payload,
        headers=headers
    )
    assert response.status_code == 200
    data = NewObjWithData(**response.json())
    assert data.name == payload['name']


@pytest.mark.smoke
@allure.feature('Basic check')
@allure.story('Get')
@allure.description('Getting of the item')
def test_get_single_item(item_id, before_after_greetings):
    with allure.step('getting the created item'):
        response = requests.get(f'{base_url}/{item_id}')
    with allure.step('check response status'):
        assert response.status_code == 200


@pytest.mark.smoke
@allure.feature('Basic check')
@allure.story('Get')
@allure.description('Getting of items')
def test_get_all():
    with allure.step('getting the created items'):
        response = requests.get(f'{base_url}')
    with allure.step('check response status'):
        assert response.status_code == 200


class DeleteSingleObject(BaseModel):
    message: str


@pytest.mark.regression
@allure.feature('Basic check')
@allure.story('Remove')
def test_delete(item_id):
    headers = {
        'Content-Type': 'application/json'
    }
    with allure.step('removing the created items'):
        response = requests.delete(f'{base_url}/{item_id}',
                                   headers=headers)
    with allure.step('check response status'):
        assert response.status_code == 200
    delete_obj = DeleteSingleObject(**response.json())
    assert 'deleted' in delete_obj.message
