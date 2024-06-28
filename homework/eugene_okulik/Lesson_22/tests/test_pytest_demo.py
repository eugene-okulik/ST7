import pytest
import requests
from pydantic import BaseModel, Field
from typing import Any


@pytest.mark.smoke
def test_get_all(session_info):
    print(session_info)
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert response.json()[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'


class Publication(BaseModel):
    userId: int
    id: int
    title: str
    body: str


def test_by_id(session_info):
    print(session_info)
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts/42')
    assert response.status_code == 200
    Publication(**response.json())


class NewObj(BaseModel):
    id: str
    name: str
    data: dict[str, Any]


class ObjData(BaseModel):
    color: str
    capacity_GB: int = Field(alias='capacity GB')


class NewObjWithData(BaseModel):
    id: str
    name: str
    data: ObjData


'''
{
    "id": "3",
    "name": "Apple iPhone 12 Pro Max",
    "data": {
        "color": "Cloudy White", 
        "capacity GB": 512
    }
}
'''


def test_hw():
    response = requests.get('https://api.restful-api.dev/objects/3')
    print(response.text)
    NewObj(**response.json())
    data = NewObjWithData(**response.json())
    print(data.data.capacity_GB)
    assert data.name == 'skdjfhskdjfh'
    assert response.json()['name'] == 'skdjfhskdjfhskjdf'


@pytest.mark.parametrize(
    'title',
    ['klsdjfhklsjdfh', 'KJSDHKSJDDS', '29834729384', '*&^^%$^&%$']
)
@pytest.mark.regression
@pytest.mark.smoke
def test_update_with_put(publication_id, session_info, title):
    print(session_info)
    payload = {
        "title": title,
        "body": "UYkajshdfkajdshfasdf-UPD",
        "userId": 1
    }

    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{publication_id}',
        json=payload
    )
    print(f'Updated publication {publication_id}')
    # assert response.json()['title'] == payload['title']
    assert response.json()['title'] == 'ksjdfhksjdfh'
