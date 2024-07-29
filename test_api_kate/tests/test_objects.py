import allure
import pytest
from test_api_kate.tests.data import payloads
from test_api_kate.endpoints.post_objects import PostObjects
from test_api_kate.endpoints.ob_by_id import ObById
from test_api_kate.endpoints.ob_put_update import ObPutUpdate
from test_api_kate.endpoints.ob_deleted import ObDeleted


@allure.feature('Main')
@allure.story('Objects')
@allure.description('Testing creating a new object')
@allure.title('Creating a new object')
def test_new_object():
    create_ob_endpoint = PostObjects()
    create_ob_endpoint.create_object(payloads.new_object)
    assert create_ob_endpoint.object_name_is_(payloads.new_object['name'])
    assert create_ob_endpoint.check_status_code_is_(200)


@allure.feature('Submain')
@allure.story('Object_ids')
def test_get_by_id(new_object):
    get_by_id = ObById()
    get_by_id.get_ob_by_id(new_object)
    assert get_by_id.check_status_code_is_(200)


@allure.feature('Submain')
@allure.story('Object_ids')
@allure.severity('Blocker')
@pytest.mark.parametrize(
    "name", ['Apple MacBook 111 Kate', 'Apple MacBook $$$ Kate', 'Apple MacBook Update Kate'],
    ids=['numbers', 'special characters', 'regular']
)
def test_change_everyth(updated_with_put, new_object, name):
    payload = payloads.put_new_object
    payload["name"] = name
    updated_with_put.ob_change_put(new_object, payload)
    assert updated_with_put.check_status_code_is_(200)
    assert updated_with_put.ob_updated_name(name)


@allure.feature('Submain')
@allure.story('Minor changes')
@allure.title('Making a single change')
def test_change_someth(updated_with_patch, new_object):
    payload = payloads.patch_new_object
    updated_with_patch.ob_change_patch(new_object, payload)
    assert updated_with_patch.check_status_code_is_(200)
    assert updated_with_patch.ob_price_check(payload['data']['price'])


@allure.feature('Main')
@allure.story('Objects')
@allure.title('Deleting newly created object')
def test_no_more_object(new_object):
    del_ob = ObDeleted()
    del_ob.ob_deleted(new_object)
    assert del_ob.check_status_code_is_(200)
