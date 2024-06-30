import pytest
import requests
from pydantic import BaseModel, Field
from typing import Any


class NewObj(BaseModel):
    id: str
    name: str
    data: dict[str, Any]


class ObjData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class NewObjWithData(BaseModel):
    id: str
    name: str
    data: ObjData


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
    NewObj(**response.json())
    data = NewObjWithData(**response.json())
    assert response.status_code == 200
    assert data.name == 'Apple MacBook Pro Kate'


@pytest.mark.critical
def test_no_more_object(new_object):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_object}')
    assert response.status_code == 200


@pytest.mark.skip('Bug 42779 ')
def test_get_by_id(new_object, session_wrap):
    response = requests.get(f'https://api.restful-api.dev/objects/{new_object}')
    assert response.status_code == 200
    assert response.json()['name'] == 'Apple MacBook Pro Kate'


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
    response = requests.put(
        f'https://api.restful-api.dev/objects/{new_object}',
        json=payload
    )
    assert response.json()['name'] == payload['name']


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
