import requests
import pytest
from pydantic import BaseModel, Field


class InsideCreationData(BaseModel):
    year: int
    price: float
    cpu_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class Creation(BaseModel):
    id: str
    name: str
    data: InsideCreationData


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

    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    Creation(**response.json())


class Deletion(BaseModel):
    message: str

@pytest.mark.regression
def test_delete_object(object_id):
    response = requests.delete(
        f'https://api.restful-api.dev/objects/{object_id}'
    )

    assert response.status_code == 200
    # Deletion(**response.json())
    answer = Deletion(**response.json())
    assert 'deleted' in answer.message


@pytest.mark.regression
@pytest.mark.smoke
def test_get_object(object_id):
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.get(
        f'https://api.restful-api.dev/objects/{object_id}',
        headers=headers
    )

    assert response.status_code == 200


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

    response = requests.put(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()['name'] == payload["name"]


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

    response = requests.patch(
        f'https://api.restful-api.dev/objects/{object_id}',
        json=payload,
        headers=headers
    )

    assert response.status_code == 200
    assert response.json()['data']['Hard disk size'] == payload['data']['Hard disk size']
    assert response.json()['data']['price'] == payload['data']['price']


@pytest.mark.skip(reason='Teacher said')
def test_to_skip(follow_the_testing_without_object):
    assert 2 == 2
