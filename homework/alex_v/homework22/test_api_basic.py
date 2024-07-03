import pytest
import requests
from pydantic import BaseModel, Field

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
def test_get_single_item(item_id, before_after_greetings):
    response = requests.get(f'{base_url}/{item_id}')
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_all():
    response = requests.get(f'{base_url}')
    assert response.status_code == 200


class DeleteSingleObject(BaseModel):
    message: str


@pytest.mark.regression
def test_delete(item_id):
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.delete(f'{base_url}/{item_id}',
                               headers=headers)
    assert response.status_code == 200
    delete_obj = DeleteSingleObject(**response.json())
    assert 'deleted' in delete_obj.message
