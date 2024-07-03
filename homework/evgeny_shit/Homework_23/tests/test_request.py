import requests
import pytest
import allure

from homework.evgeny_shit.Homework_23.client import URL, create_payload


@allure.feature("Old create object")
@pytest.mark.critical
def test_create_object(session_info):
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    response = requests.post(URL, json=payload)

    response_data = response.json()
    assert response_data['name'] == payload['name'], f"Expected name {payload['name']}, got {response_data['name']}"
    for key, value in payload['data'].items():
        assert response_data['data'][key] == value, f"Expected {key} {value}, got {response_data['data'][key]}"

    obj_id = response_data['id']
    delete_response = requests.delete(f"{URL}/{obj_id}")
    assert delete_response.status_code == 200, f"Expected status code 200, got {delete_response.status_code}"


@allure.feature("Old get object")
@pytest.mark.smoke
def test_get_object(object_id, session_info):
    response = requests.get(f"{URL}/{object_id}")

    response_data = response.json()
    assert response_data['id'] == object_id, f"Expected id {object_id}, got {response_data['id']}"
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@allure.feature("Old update object")
def test_update_object(object_id, session_info):
    payload = create_payload("Desktop", 2002, 0, "Intel Celeron (Pentium 4) 2.0", "1.8 GB")
    response = requests.put(f"{URL}/{object_id}", json=payload)

    response_data = response.json()
    assert response_data['name'] == payload['name'], f"Expected name {payload['name']}, got {response_data['name']}"
    for key, value in payload['data'].items():
        assert response_data['data'][key] == value, f"Expected {key} {value}, got {response_data['data'][key]}"


@allure.feature("Old partial update object")
def test_partial_update_object(object_id, session_info):
    payload = {"name": "(Updated Name)"}
    response = requests.patch(f"{URL}/{object_id}", json=payload)

    response_data = response.json()
    assert response_data['name'] == payload['name'], f"Expected name {payload['name']}, got {response_data['name']}"


@allure.feature("Old delete object")
def test_delete_object(object_id_without_del, session_info):
    response = requests.delete(f"{URL}/{object_id_without_del}")

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
