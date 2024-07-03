import allure
import pytest

from homework.evgeny_shit.Homework_23.client import (
    create_payload, validate_response_data, send_put_request, send_patch_request,
    send_post_request, send_get_request, send_delete_request, attach_response
)
from homework.evgeny_shit.Homework_23.models import ResponseModel, DeleteResponseModel


@allure.title("Create object test")
@allure.feature("Create object")
@allure.story("POST")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test checks creating a publication')
@pytest.mark.critical
def test_create_object(session_info):
    payload = create_payload("Apple MacBook Pro 16", 2019, 1849.99, "Intel Core i9", "1 TB")
    with allure.step("Send POST request to create object"):
        response = send_post_request(payload)
        attach_response(response, "Response")

    response_data = response.json()

    with allure.step("Validate response data"):
        validated_response = ResponseModel(**response_data)
        validate_response_data(validated_response, payload)

    obj_id = validated_response.id

    with allure.step("Send DELETE request to clean up"):
        delete_response = send_delete_request(obj_id)
        attach_response(delete_response, "Delete Response")

    with allure.step("Validate delete response status code"):
        assert delete_response.status_code == 200, f"Expected status code 200, got {delete_response.status_code}"
    with allure.step("Validate delete response message"):
        assert "has been deleted" in delete_response.json()['message'], \
            f"Expected message to contain 'has been deleted', got {delete_response.json()['message']}"


@allure.title("Get object test")
@allure.feature("Get object")
@allure.story("GET")
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test checks getting a publication')
@pytest.mark.smoke
def test_get_object(object_id: str, session_info):
    with allure.step("Send GET request to retrieve object"):
        response = send_get_request(object_id)
        attach_response(response, "Response")

    response_data = response.json()

    with allure.step("Validate response id field"):
        assert response_data['id'] == object_id, f"Expected id {object_id}, got {response_data['id']}"
    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@allure.title("Get all objects test")
@allure.feature("Get all objects")
@allure.story("GET")
@allure.severity(allure.severity_level.MINOR)
@allure.description('This test checks getting all publications')
@pytest.mark.skip(reason="Just has to be skipped")
def test_get_all_objects(session_info):
    with allure.step("Send GET request to retrieve all objects"):
        response = send_get_request('')
        attach_response(response, "Response")

    response_data = response.json()

    with allure.step("Validate response length"):
        assert len(response_data) > 0, f"Expected at least one object, got {len(response_data)}"
    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"


@allure.title("Update object test")
@allure.feature("Update object")
@allure.story("PUT")
@allure.severity(allure.severity_level.NORMAL)
@allure.description('This test checks updating a publication')
@pytest.mark.parametrize(
    "data",
    [
        create_payload("apple macbook pro 16", 2019, 1849.99, "intel core i9", "1 tb"),
        create_payload("APPLE MACBOOK PRO 16", 2019, 1849.99, "INTEL CORE I9", "1 TB"),
        create_payload("Аппле Макбук Про 16", 2019, 1849.99, "Интел Кор И9", "1 ТБ"),
    ], ids=['lowercase', 'uppercase', 'rus']
)
def test_update_object(object_id: str, session_info, data: dict):
    payload = data
    with allure.step("Send PUT request to update object"):
        response = send_put_request(object_id, payload)
        attach_response(response, "Response")

    response_data = response.json()

    with allure.step("Validate response data"):
        validated_response = ResponseModel(**response_data)
        validate_response_data(validated_response, payload)


@allure.title("Partial update object test")
@allure.feature("Partial update object")
@allure.story("PATCH")
@allure.description('This test checks partial updating a publication')
@allure.severity(allure.severity_level.NORMAL)
def test_partial_update_object(object_id: str, session_info):
    payload = {"name": "(Updated Name)"}
    with allure.step("Send PATCH request to partially update object"):
        response = send_patch_request(object_id, payload)
        attach_response(response, "Response")

    response_data = response.json()

    with allure.step("Validate response data"):
        validated_response = ResponseModel(**response_data)

    with allure.step("Validate updated name"):
        assert validated_response.name == payload['name'], (f"Expected name {payload['name']}, "
                                                            + f"got {validated_response.name}")


@allure.title("Delete object test")
@allure.feature("Delete object")
@allure.story("DELETE")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description('This test checks deleting a publication')
@pytest.mark.critical
def test_delete_object(object_id_without_del: str, session_info):
    with allure.step("Send DELETE request to delete object"):
        response = send_delete_request(object_id_without_del)
        attach_response(response, "Delete Response")

    response_data = response.json()

    with allure.step("Validate delete response"):
        validated_response = DeleteResponseModel(**response_data)

    with allure.step("Validate response status code"):
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    with allure.step("Validate response message"):
        assert "has been deleted" in validated_response.message, \
            f"Expected message to contain 'has been deleted', got {validated_response.message}"
