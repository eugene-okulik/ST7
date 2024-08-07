import allure
import pytest

from test_api_alex_v_project.endpoints.post_item import PostItem
from test_api_alex_v_project.tests.data import payloads


@allure.feature('item creation function')
@allure.story('Create implementation')
def test_create_item():
    create_item_endpoint = PostItem()
    create_item_endpoint.create_item(payloads.new_item_payload)
    assert create_item_endpoint.check_status_code_is_(200)
    assert create_item_endpoint.check_response_title_is_(payloads.new_item_payload['name'])


@allure.feature('Item adjusting function')
@allure.story('Change implementation')
@pytest.mark.parametrize('name',
                         ['SONY ERICSSON',
                          '12345',
                          '!@#$%^&'])
def test_update_item(put_item_endpoint, item_id, name):
    payload = payloads.put_new__payload
    payload['name'] = name
    put_item_endpoint.update_item(item_id, payload)
    assert put_item_endpoint.check_status_code_is_(200)


@allure.feature('Item partial changing function')
@allure.story('Change implementation')
def test_partial_item_update(patch_item_endpoint, item_id):
    patch_item_endpoint.partial_update_item(payloads.put_new__payload, item_id)
    assert patch_item_endpoint.check_status_code_is_(200)


@allure.title('Get item by id')
@allure.feature('ID object usage')
def test_get_item_by_id(get_item_endpoint, item_id):
    get_item_endpoint.get_item_by_id(item_id)
    with allure.step('Check response status'):
        assert get_item_endpoint.check_status_code_is_(200)


@allure.title('Delete item by id')
@allure.feature('ID object usage')
def test_delete_item_by_id(delete_item_endpoint, item_id):
    delete_item_endpoint.delete_item_by_id(item_id)
    assert delete_item_endpoint.check_status_code_is_(200)
