import pytest
import requests
from pydantic import BaseModel, Field
import allure


class ObjData(BaseModel):
    year: int
    price: str
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class NewObjWithData(BaseModel):
    name: str
    data: ObjData


class DelNewObjWithData(BaseModel):
    message: str


@allure.feature('Critical test')
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
    data = NewObjWithData(**response.json())
    assert data.name == data.name


@allure.feature('Test update')
@allure.story('Update')
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


@allure.feature('Test update')
@allure.story('Update')
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


@allure.feature('Smoke test')
@allure.story('get_id')
def test_get_id(new_obj, session_info):
    with allure.step('Execute query'):
        response = requests.request('GET', f'https://api.restful-api.dev/objects/{new_obj}')
    with allure.step('Comparison name'):
        assert response.json()['name'] == 'NarateL'
    assert response.status_code == 200


@allure.feature('Test delete')
@allure.title('Проверка удаления')
@pytest.mark.smoke
def test_delete_obj(new_obj, session_info):
    with allure.step('Execute query'):
        response = requests.delete(f'https://api.restful-api.dev/objects/{new_obj}')
    with allure.step('status code'):
        assert response.status_code == 200
    delete_obj = DelNewObjWithData(**response.json())
    assert delete_obj.message == delete_obj.message


@allure.feature('Test redirect')
@allure.story('Comparison')
@allure.title('Тест на редирект')
def test_redirect():
    url = 'https://sreda.ru/'
    response = requests.get(url, allow_redirects=False)
    if response.status_code == 301 or response.status_code == 302:
        print(f"Редирект: {response.headers['Location']}")
    else:
        print(f"Редирект не обнаружен. Код статуса: {response.status_code}")
