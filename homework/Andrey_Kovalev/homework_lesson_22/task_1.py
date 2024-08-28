import pytest
import requests
from pydantic import BaseModel, Field


class ObjData(BaseModel):
    year: int
    price: float
    name: str = Field(alias='name')


class NewObjWithData(BaseModel):
    name: str
    data: ObjData


class DelNewObjWithData(BaseModel):
    message: str


@pytest.mark.critical
def test_new_object():
    payload = {
        "name": "TOYOTA",
        "data": {
            "year": 2019,
            "price": 1849.99,
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
    data = NewObjWithData(**response.json())
    assert data.name == payload["name"]  # Исправлено


@pytest.mark.parametrize(
    'name',
    ['dimon', 'sane4ek1337', '88005553535'],
    ids=['lowercase', 'uppercase', 'numbers']
)
def test_update_obj(new_obj, session_info, name):
    payload = {
        "name": name,
        "data": {
            "year": 2019,
            "price": 1849.99,
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
         "name": "TOYOTA",
         "data": {
            "year": 1996,
            "price": 1337.0
         }
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{new_obj}',
        json=payload
    )
    assert response.status_code == 200
    assert response.json()['name'] == payload['name']


@pytest.mark.skip(reason='bag #12')
def test_get_id(new_obj, session_info):
    response = requests.request('GET', f'https://api.restful-api.dev/objects/{new_obj}')
    assert response.json()['name'] == 'TOYOTA'
    assert response.status_code == 200


@pytest.mark.smoke
def test_delete_obj(new_obj, session_info):
    response = requests.delete(f'https://api.restful-api.dev/objects/{new_obj}')
    assert response.status_code == 200
    delete_obj = DelNewObjWithData(**response.json())
    assert delete_obj.message == "Expected message"
