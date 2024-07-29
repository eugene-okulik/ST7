import pytest
import requests
from pydantic import BaseModel, Field


url = 'https://api.restful-api.dev/objects'


class ObjectData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class NewObjectData(BaseModel):
    id: str
    name: str
    createdAt: str
    data: ObjectData


def test_create_object_post(get_object_id, session_info):
    print(session_info)
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
    assert response.status_code == 200
    data = NewObjectData(**response.json())
    assert data.name == payload['name']


def test_get_object_by_id(get_object_id, session_info):
    print(session_info)
    response = requests.get(f'{url}/{get_object_id}')
    assert response.status_code == 200


@pytest.mark.parametrize(
    'name', ['Apple MacBook Pro 16', 'APPLE MACBOOK PRO 16', 'apple macbook pro 16']
)
@pytest.mark.parametrize(
    'year', [2019, 1990, 3050]
)
@pytest.mark.parametrize(
    'color', ['silver', 'SILVER', 'SiLvEr']
)
@pytest.mark.smoke
def test_update_object_put(get_object_id, session_info, name, year, color):
    print(session_info)
    payload = {
        "name": name,
        "data": {
            "year": year,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": color
        }
    }
    response = requests.put(
        f'{url}/{get_object_id}',
        json=payload
    )
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']
    assert response.json()['data']['year'] == payload['data']['year']
    assert response.json()['data']['color'] == payload['data']['color']


@pytest.mark.skip(reason='Bug #1')
@pytest.mark.critical
def test_update_object_price(get_object_id, session_info):
    print(session_info)
    payload = {
        "data": {
            "price": 3000
        }
    }
    response = requests.patch(
        f'{url}/{get_object_id}',
        json=payload
    )
    assert response.status_code == 200
    assert response.json()['data']['price'] == payload['data']['price']


@pytest.mark.critical
def test_partially_update_object_patch(get_object_id, session_info):
    print(session_info)
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(
        f'{url}/{get_object_id}',
        json=payload
    )
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']


class DeleteObjData(BaseModel):
    message: str


def test_delete_object(get_object_id, session_info):
    print(session_info)
    response = requests.delete(f'{url}/{get_object_id}')

    assert response.status_code == 200
    delete_data = DeleteObjData(**response.json())
    assert "has been deleted" in delete_data.message
