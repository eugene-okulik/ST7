import requests
import pytest
from pydantic import BaseModel, Field


class Data(BaseModel):
    year: int
    price: float
    cpu_model: str = Field(alias='CPU model')
    hard_disk_size: str = Field(alias='Hard disk size')


class Publication(BaseModel):
    id: str
    name: str
    createdAt: str
    data: Data


class DelPublication(BaseModel):
    message: str


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
        publication = Publication(**response.json())
        assert response.status_code == 200, "Status code is not 200"
        assert publication.name == payload['name']
        assert publication.data.price == payload['data']['price']

    def test_get_object_by_id(self, object_id):
        response = requests.get(url=f"{self.BASE_URL}/{object_id}")

        assert response.status_code == 200, "Status code is not 200"
        assert response.json().get('id') == object_id

    @pytest.mark.parametrize(
        'payload',
        [
            {
                "name": "ASUS BOOK",
                "data": {
                    "year": 2020,
                    "price": 1500,
                    "CPU model": "Intel Core i666",
                    "Hard disk size": "2 TB"
                }
            },
            {
                "name": "Xiaomi",
                "data": {
                    "year": 1999,
                    "price": 500,
                    "CPU model": "Intel Core i0",
                    "Hard disk size": "500 Gb"
                }
            },
            {
                "name": "KakoyToBook",
                "data": {
                    "year": 2025,
                    "price": 5500,
                    "CPU model": "Intel Core i999",
                    "Hard disk size": "200 TB"
                }
            },
        ]
    )
    def test_change_object_put(self, object_id, payload):
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

    def test_delete_object(self, object_id):
        response = requests.delete(url=f"{self.BASE_URL}/{object_id}")

        assert response.status_code == 200, "Status code is not 200"
        del_publication = DelPublication(**response.json())

        assert "has been deleted" in del_publication.message

    @pytest.mark.skip
    def test_delete_non_existent_object(self, object_id):
        response = requests.delete(url=f"{self.BASE_URL}/999")

        assert response.status_code == 404, "Status code is not 404"
