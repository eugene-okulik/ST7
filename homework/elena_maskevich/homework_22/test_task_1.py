# Продолжим оформлять тесты из предыдущих заданий
# Тест на изменение объекта с помощью метода PUT оформите так, чтобы он тестировал 3 разных изменения
# с помощью parametrize
# Создайте еще один любой тест и пометьте, что его нужно пропустить (skip)
# Разделите тесты на 2 файла, вынесите фикстуры в файл conftest.py.
# С помощью Pydantic провалидируйте схему ответов для POST и DELETE запросов.

import requests
import pytest

base_url = 'https://api.restful-api.dev/objects'


@pytest.mark.smoke
def test_get_by_id(object_id, session_info):
    response = requests.get(f'{base_url}/{object_id}')
    assert response.status_code == 200, 'Incorrect status code'
    print(f'Object with id {object_id}')


@pytest.mark.parametrize('year', [2, 10, 2999999])
@pytest.mark.critical
def test_update_with_put(object_id, session_info, year):
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": year,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
    }

    response = requests.put(
        f'{base_url}/{object_id}',
        json=payload
    )

    assert response.status_code == 200, 'Incorrect status code'
    print(f'Updated put object with id {object_id}')
