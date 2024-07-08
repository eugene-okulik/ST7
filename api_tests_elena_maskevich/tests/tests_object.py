import allure
import pytest

from api_tests_elena_maskevich.tests.data import payloads
from api_tests_elena_maskevich.conftest import (object_id, get_object_id, create_object_id, put_object_id,
                                                patch_object_id, deleted_object_id)
base_url = 'https://api.restful-api.dev/objects'


@allure.title('Getting object by id')
@allure.feature('Use ID to get object')
@allure.story('New')
@allure.parent_suite('Suite - test object by id')
@pytest.mark.smoke
def test_get_by_id(get_object_id, object_id):
    get_object_id.get_object(object_id)
    assert get_object_id.check_status_code_(200)


@allure.feature('Object testing')
@allure.story('Object')
@pytest.mark.parametrize('year', [2, 10, 2999999])
@pytest.mark.critical
def test_update_with_put(put_object_id, object_id,  year):
    payload = payloads.put_payload
    payload['data']['year'] = year
    put_object_id.put_object(object_id, payload)


@allure.feature('Task2')
@allure.story('Object2')
def test_create_object(create_object_id):
    create_object_id.create_object(payloads.payload)
    assert create_object_id.check_status_code_(200)
    assert create_object_id.check_response_name(payloads.payload['name'])


@allure.feature('Task2')
@allure.story('Object2')
def test_change_object_patch(patch_object_id, object_id):
    patch_object_id.patch_object(payloads.patch_payload, object_id)
    assert patch_object_id.check_status_code_(200)


@allure.feature('Task2')
@allure.story('Object2')
def test_delete_obj_by_id(deleted_object_id, object_id):
    deleted_object_id.delete_object(object_id)
    assert deleted_object_id.check_status_code_(200)