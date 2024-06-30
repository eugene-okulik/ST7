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


def test_get_single_item(item_id, before_after_greetings):
    response = requests.get(f'{base_url}/{item_id}')
    assert response.status_code == 200


@pytest.mark.smoke
def test_get_all():
    response = requests.get(f'{base_url}')
    assert response.status_code == 200


@pytest.mark.regression
def test_delete(item_id):
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.delete(f'{base_url}/{item_id}',
                               headers=headers)
    assert data == NewObjWithData(**response.json())
    print(data.data)
