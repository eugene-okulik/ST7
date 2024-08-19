import pytest
import requests

from homework.evgeny_shit.Homework_23.client import URL, create_payload


@pytest.fixture
def object_id():
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    response = requests.post(URL, json=payload)
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f"{URL}/{obj_id}")


@pytest.fixture
def object_id_without_del():
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    response = requests.post(URL, json=payload)
    obj_id = response.json()['id']
    return obj_id
