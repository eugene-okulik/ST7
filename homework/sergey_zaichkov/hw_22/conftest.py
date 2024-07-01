import pytest
import requests


@pytest.fixture(scope='session', autouse=True)
def start_completed():
    print("\nStart testing")
    yield
    print("\nTesting completed")


@pytest.fixture()
def object_id():
    url = "https://api.restful-api.dev/objects"
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post(url=url, json=payload)
    assert response.status_code == 200, "Status code is not 200"
    response_dict = response.json()
    obj_id = response_dict.get('id')

    yield obj_id

    if requests.get(f"{url}/{obj_id}").status_code == 200:
        response = requests.delete(url=f"{url}/{obj_id}")
        assert response.status_code == 200, "Status code is not 200"
