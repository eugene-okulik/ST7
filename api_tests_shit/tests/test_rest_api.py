import allure
import pytest

from api_tests_shit.client import allure_annotations
from api_tests_shit.tests.data import payloads


@allure_annotations(
    title="Create object test",
    story="POST",
    description='This test checks creating a publication',
    severity=allure.severity_level.CRITICAL,
    tag='!!!'
)
@pytest.mark.critical
def test_create_object(create_obj_endpoint, session_info):
    create_obj_endpoint.create_object(payloads.create_obj)
    assert create_obj_endpoint.check_status_code(create_obj_endpoint.response, 200)
    assert create_obj_endpoint.check_response_name_is_(payloads.create_obj['name'])
    assert create_obj_endpoint.check_response_message_is_("has been deleted")


@allure_annotations(
    title="Get object test",
    story="GET",
    description='This test checks getting a publication'
)
@pytest.mark.smoke
def test_get_object(get_obj_endpoint, object_id, session_info):
    get_obj_endpoint.get_single_obj(object_id)
    assert get_obj_endpoint.check_response_id_is_(object_id)
    assert get_obj_endpoint.check_status_code(get_obj_endpoint.response, 200)


@allure_annotations(
    title="Get all objects test",
    story="GET",
    description='This test checks getting all publications',
    tag='skipped',
    severity=allure.severity_level.MINOR
)
@pytest.mark.skip(reason="Just has to be skipped")
def test_get_all_objects(get_all_obj_endpoint, session_info):
    get_all_obj_endpoint.get_all_obj()
    assert get_all_obj_endpoint.check_status_code(get_all_obj_endpoint.response, 200)
    assert get_all_obj_endpoint.check_response_is_not_empty()


@allure_annotations(
    title="Update object test",
    story="PUT",
    description='This test checks updating a publication'
)
@pytest.mark.parametrize(
    "request_data",
    [
        payloads.update_obj_lower,
        payloads.update_obj_upper,
        payloads.update_obj_rus
    ], ids=['lowercase', 'uppercase', 'rus']
)
def test_update_object(update_obj_endpoint, request_data, object_id, session_info):
    update_obj_endpoint.update_object(request_data, object_id)
    assert update_obj_endpoint.check_status_code(update_obj_endpoint.response, 200)
    assert update_obj_endpoint.check_response_name_is_(request_data['name'])
    assert update_obj_endpoint.check_response_cpu_model_is_(request_data['data']['CPU model'])


@allure_annotations(
    title="Partial update object test",
    story="PATCH",
    description='This test checks partial updating a publication'
)
def test_partial_update_object(partial_update_obj_endpoint, object_id, session_info):
    partial_update_obj_endpoint.part_update_object(payloads.partial_update_obj, object_id)
    assert partial_update_obj_endpoint.check_status_code(partial_update_obj_endpoint.response, 200)
    assert partial_update_obj_endpoint.check_response_name_is_(payloads.partial_update_obj['name'])


@allure_annotations(
    title="Delete object test",
    story="DELETE",
    description='This test checks deleting a publication',
    tag='!!!',
    severity=allure.severity_level.CRITICAL
)
@pytest.mark.critical
def test_delete_object(delete_obj_endpoint, object_id, session_info):
    delete_obj_endpoint.delete_object(object_id)
    assert delete_obj_endpoint.check_status_code(delete_obj_endpoint.delete_response, 200)
    assert delete_obj_endpoint.check_response_message_is_("has been deleted")
