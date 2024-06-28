import requests
import pytest

from ..client import URL, create_payload, validate_response_data
from ..models import ResponseModel, DeleteResponseModel


@pytest.mark.critical
def test_create_object(session_info):
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    response = requests.post(URL, json=payload)
    response_data = response.json()

    validated_response = ResponseModel(**response_data)

    validate_response_data(validated_response, payload)

    obj_id = validated_response.id
    delete_response = requests.delete(f"{URL}/{obj_id}")
    assert delete_response.status_code == 200, f"Expected status code 200, got {delete_response.status_code}"


@pytest.mark.smoke
def test_get_object(object_id, session_info):
    response = requests.get(f"{URL}/{object_id}")
    response_data = response.json()

    assert response_data['id'] == object_id, f"Expected id {object_id}, got {response_data['id']}"
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@pytest.mark.skip(reason="Just has to be skipped")
def test_get_all_object(session_info):
    response = requests.get(URL)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@pytest.mark.parametrize(
    "data",
    [
        create_payload("apple macbook pro 16", 2019, 1849.99, "intel core i9", "1 tb"),
        create_payload("APPLE MACBOOK PRO 16", 2019, 1849.99, "INTEL CORE I9", "1 TB"),
        create_payload("Аппле Макбук Про 16", 2019, 1849.99, "Интел Кор И9", "1 ТБ"),
    ], ids=['lowercase', 'uppercase', 'rus']
)
def test_update_object(object_id, session_info, data):
    payload = data
    response = requests.put(f"{URL}/{object_id}", json=payload)
    response_data = response.json()

    validated_response = ResponseModel(**response_data)
    validate_response_data(validated_response, payload)


def test_partial_update_object(object_id, session_info):
    payload = {"name": "(Updated Name)"}
    response = requests.patch(f"{URL}/{object_id}", json=payload)
    response_data = response.json()

    validated_response = ResponseModel(**response_data)
    assert validated_response.name == payload['name'], f"Expected name {payload['name']}, got {validated_response.name}"


def test_delete_object(object_id_without_del, session_info):
    response = requests.delete(f"{URL}/{object_id_without_del}")
    response_data = response.json()

    validated_response = DeleteResponseModel(**response_data)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert "has been deleted" in validated_response.message, \
        f"Expected message to contain 'has been deleted', got {validated_response.message}"
