import requests
import pytest


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


class TestRestfulApi:
    BASE_URL = "https://api.restful-api.dev/objects"

    def test_add_object(self):
        payload = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2019,
                "price": 1849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB"
            }
        }
        response = requests.post(url=self.BASE_URL, json=payload)
        assert response.status_code == 200, "Status code is not 200"

    @pytest.mark.smoke
    def test_get_object_by_id(self, object_id):
        response = requests.get(url=f"{self.BASE_URL}/{object_id}")

        assert response.status_code == 200, "Status code is not 200"
        assert response.json().get('id') == object_id

    def test_change_object_put(self, object_id):
        payload = {
            "name": "ASUS BOOK",
            "data": {
                "year": 2020,
                "price": 1500,
                "CPU model": "Intel Core i666",
                "Hard disk size": "2 TB"
            }
        }
        response = requests.put(url=f"{self.BASE_URL}/{object_id}", json=payload)

        assert response.status_code == 200, "Status code is not 200"
        response_dict = response.json()
        assert payload['name'] == response_dict.get('name')
        assert payload['data']['year'] == response_dict.get('data')['year']

    def test_change_object_patch(self, object_id):
        payload = {"name": "ULTRA MEGA SUPER BOOK-PUK"}
        response = requests.patch(url=f"{self.BASE_URL}/{object_id}", json=payload)

        assert response.status_code == 200, "Status code is not 200"
        response_dict = response.json()
        assert payload['name'] == response_dict.get('name')

    @pytest.mark.critical
    def test_delete_object(self, object_id):
        response = requests.delete(url=f"{self.BASE_URL}/{object_id}")

        assert response.status_code == 200, "Status code is not 200"
        response_dict = response.json()
        assert "has been deleted" in response_dict.get('message')
