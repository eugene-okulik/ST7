import pytest
import allure
from api_tests_tumanov.tests.data import payloads

name_update_put = payloads.put_update_obj
name_cheng_patch = payloads.patch_obj_change['name']


def test_obj_create(create_obj_endpoint):
    create_obj_endpoint.create_object(payload=payloads.new_object)
    create_obj_endpoint.check_status_code_is_(200)
    create_obj_endpoint.check_response_name_is_(payloads.new_object.get('name'))


@allure.feature('Test update put')
@allure.story('Update')
def test_update_obj(new_obj, put_update_endpoint):
    put_update_endpoint.put_update(new_obj, payloads.put_update_obj)
    put_update_endpoint.check_status_code_is_(200)
    put_update_endpoint.check_response_name_is_(payloads.put_update_obj['name'])


@allure.feature('Test change')
@pytest.mark.parametrize('key', ['price'])
@pytest.mark.smoke
def test_change_obj(new_obj, patch_change_endpoint, key):
    patch_change_endpoint.patch_change_obj(new_obj, payloads.patch_obj_change)
    patch_change_endpoint.check_status_code_is_(200)
    patch_change_endpoint.check_response_name_is_(payloads.patch_obj_change['name'])


@allure.story('get_id')
def test_get_id(get_obj_endpoint, new_obj):
    get_obj_endpoint.get_obj_id(new_obj)
    get_obj_endpoint.check_response_name_is_(payloads.new_object['name'])
    get_obj_endpoint.check_status_code_is_(200)


@allure.feature('Test delete')
@allure.title('Проверка удаления')
@pytest.mark.smoke
def test_delete_obj(delete_obj_endpoint, new_obj):
    delete_obj_endpoint.delete_obj(new_obj)
    delete_obj_endpoint.check_status_code_is_(200)
