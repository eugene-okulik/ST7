import os
import requests
import pytest
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('BASE_URL')


@pytest.fixture()
def session_info():
    print('\nStart testing')
    yield
    print('\nTesting completed')


@pytest.fixture
def create_delete_object():
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    response = requests.post(URL, json=payload)
    response.raise_for_status()
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f"{URL}/{obj_id}")


@pytest.fixture
def create_object():
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    response = requests.post(URL, json=payload)
    response.raise_for_status()
    obj_id = response.json()['id']
    yield obj_id
    requests.delete(f"{URL}/{obj_id}")


def create_payload(name, year, price, cpu_model, hard_disk_size, color=None):
    data = {
        "year": year,
        "price": price,
        "CPU model": cpu_model,
        "Hard disk size": hard_disk_size,
    }
    if color:
        data["color"] = color
    return {
        "name": name,
        "data": data
    }


@pytest.mark.critical
def test_create_object(session_info):
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    response = requests.post(URL, json=payload)
    response.raise_for_status()

    response_data = response.json()
    assert response_data['name'] == payload['name'], f"Expected name {payload['name']}, got {response_data['name']}"
    for key, value in payload['data'].items():
        assert response_data['data'][key] == value, f"Expected {key} {value}, got {response_data['data'][key]}"

    obj_id = response_data['id']
    delete_response = requests.delete(f"{URL}/{obj_id}")
    delete_response.raise_for_status()
    assert delete_response.status_code == 200, f"Expected status code 200, got {delete_response.status_code}"


@pytest.mark.smoke
def test_get_object(create_delete_object, session_info):
    response = requests.get(f"{URL}/{create_delete_object}")
    response.raise_for_status()

    response_data = response.json()
    assert response_data['id'] == create_delete_object, f"Expected id {create_delete_object}, got {response_data['id']}"
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


def test_update_object(create_delete_object, session_info):
    payload = create_payload("Desktop", 2002, "free", "Intel Celeron (Pentium 4) 2.0", "1.8 GB", "silver")
    response = requests.put(f"{URL}/{create_delete_object}", json=payload)
    response.raise_for_status()

    response_data = response.json()
    assert response_data['name'] == payload['name'], f"Expected name {payload['name']}, got {response_data['name']}"
    for key, value in payload['data'].items():
        assert response_data['data'][key] == value, f"Expected {key} {value}, got {response_data['data'][key]}"


def test_partial_update_object(create_delete_object, session_info):
    payload = {"name": "(Updated Name)"}
    response = requests.patch(f"{URL}/{create_delete_object}", json=payload)
    response.raise_for_status()

    response_data = response.json()
    assert response_data['name'] == payload['name'], f"Expected name {payload['name']}, got {response_data['name']}"


def test_delete_object(create_object, session_info):
    response = requests.delete(f"{URL}/{create_object}")
    response.raise_for_status()

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
