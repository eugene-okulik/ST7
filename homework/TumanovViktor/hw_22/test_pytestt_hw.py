import pytest
import requests
from pydantic import BaseModel, Field
from typing import Any


@pytest.mark.critical
def test_new_obj():
    payload = {
        "name": "NarateL",
        "data": {
            "year": 30,
            "price": "100$",
            "CPU model": "World 2024",
            "Hard disk size": "8880 TB"
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
    print(f'Обьект успешно создан {response.json()["id"]}')


@pytest.mark.parametrize(
    'name',
    ['asdfsdfsdf', 'SDFSKJDFKSJ', '1234567890'],
    ids=['lowercase', 'uppercase', 'numbers']
)
def test_update_obj(new_obj, session_info, name):
    payload = {
        "name": "NarateL",
        "data": {
            "year": 1223,
            "price": "77770$",
            "CPU model": "World 2024",
            "Hard disk size": "1000 TB",
            "color": "Green"
        }
    }
    response = requests.put(f'https://api.restful-api.dev/objects/{new_obj}',
                            json=payload
                            )
    assert response.status_code == 200


@pytest.mark.smoke
def test_change_obj(new_obj, session_info):
    payload = {
        "name": "NarateL",
        "data": {
            "year": 10,
            "price": "5000$"
        }
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_obj}',
        json=payload
    )
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']


class Publication(BaseModel):
    name: str
    data: dict[str, Any]


class ObjData(BaseModel):
    year: int
    price: str
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class NewObjWithData(BaseModel):
    name: str
    data: ObjData


def test_get_id(new_obj, session_info):
    response = requests.request('GET', f'https://api.restful-api.dev/objects/{new_obj}')
    assert response.json()['name'] == 'NarateL'
    assert response.status_code == 200
    assert response.json()['id'] == new_obj
    print(response.json())
    Publication(**response.json())
    data = NewObjWithData(**response.json())
    print(data.data.year)


def test_delete_obj(new_obj, session_info):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_obj}')
    assert response.status_code == 200


@pytest.mark.skip(reason='bag #12')
@pytest.mark.smoke
def test_one():
    assert 2 == 2
