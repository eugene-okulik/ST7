import requests
import pytest
from pydantic import BaseModel, Field
import allure


class InsideCreationData(BaseModel):
    year: int
    price: float
    cpu_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class Creation(BaseModel):
    id: str
    name: str
    data: InsideCreationData


class Deletion(BaseModel):
    message: str


@allure.description('Check creating Post')
@allure.feature('With one object')
@allure.story('POST')
@allure.title('Create Post')
@pytest.mark.regression
def test_create_object(follow_the_testing_without_object):

    payload = {
        "name": "Asus Ultrabook 2",
        "data": {
            "year": 2021,
            "price": 837.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "1 TB"
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    with allure.step('Make request'):
        response = requests.post(
            'https://api.restful-api.dev/objects',
            json=payload,
            headers=headers
        )
    with allure.step('Check response status'):
        assert response.status_code == 200
    with allure.step('Check response shema'):
        Creation(**response.json())


@allure.description('Check deleting Post')
@allure.feature('With one object')
@allure.story('DEL')
@allure.title('Delete Post')
@pytest.mark.regression
def test_delete_object(object_id):
    with allure.step('Make request'):
        response = requests.delete(
            f'https://api.restful-api.dev/objects/{object_id}'
        )

    with allure.step('Check response status'):
        assert response.status_code == 200
    # Deletion(**response.json())
    with allure.step('Check right answer in response'):
        answer = Deletion(**response.json())
        assert 'deleted' in answer.message


@allure.description('Check created Post')
@allure.feature('With one objectt')
@allure.story('GET')
@allure.title('Watch Post')
@pytest.mark.regression
@pytest.mark.smoke
def test_get_object(object_id):
    headers = {
        'Content-Type': 'application/json'
    }

    with allure.step('Make request'):
        response = requests.get(
            f'https://api.restful-api.dev/objects/{object_id}',
            headers=headers
        )

    with allure.step('Check response status'):
        assert response.status_code == 200


@allure.description('Check all Posts')
@allure.feature('All objects')
@allure.story('GET')
@allure.title('Watch all Posts')
@pytest.mark.regression
@pytest.mark.smoke
def test_get_object(follow_the_testing_without_object):
    headers = {
        'Content-Type': 'application/json'
    }

    with allure.step('Make request'):
        response = requests.get(
            f'https://api.restful-api.dev/objects',
            headers=headers
        )

    with allure.step('Check response status'):
        assert response.status_code == 200


@allure.description('Check updating Post')
@allure.feature('With one object')
@allure.story('PUT')
@allure.title('Change Post')
@pytest.mark.parametrize('price', [199.9, '297.3', -100, 'handred bucks'])
@pytest.mark.regression
@pytest.mark.critical
def test_update_object(object_id, price):

    payload = {
        "name": "Asus Ultrabook 2a",
        "data": {
            "year": 2022,
            "price": price,
            "CPU model": "Intel Core i3",
            "Hard disk size": "128 Mb"
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    with allure.step('Make request'):
        response = requests.put(
            f'https://api.restful-api.dev/objects/{object_id}',
            json=payload,
            headers=headers
        )

    with allure.step('Check response status'):
        assert response.status_code == 200
    with allure.step('Check right name in response'):
        assert response.json()['name'] == payload["name"]


@allure.description('Check partually updating Post')
@allure.feature('With one object')
@allure.story('PATCH')
@allure.title('Cnahge the part of Post')
@pytest.mark.regression
def test_partually_update_object(object_id):

    payload = {
        "data": {
            "Hard disk size": "256 Mb",
            "price": 1837.99,
        }
    }

    headers = {
        'Content-Type': 'application/json'
    }

    with allure.step('Make request'):
        response = requests.patch(
            f'https://api.restful-api.dev/objects/{object_id}',
            json=payload,
            headers=headers
        )

    with allure.step('Check response status'):
        assert response.status_code == 200
    with allure.step('Check right hard disk size in response'):
        assert response.json()['data']['Hard disk size'] == payload['data']['Hard disk size']
    with allure.step('Check right price in response'):
        assert response.json()['data']['price'] == payload['data']['price']
