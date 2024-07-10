import allure
import pytest

from test_api_alex_v_project.endpoints.get_item import GetById
from test_api_alex_v_project.endpoints.post_item import PostItem
from test_api_alex_v_project.tests.data import payloads


def test_create_item():
    create_item_endpoint = PostItem()
    create_item_endpoint.create_item(payloads.new_item_payload)
    assert create_item_endpoint.check_status_code_is_(200)
    assert create_item_endpoint.check_response_title_is_(payloads.new_item_payload['name'])


@pytest.mark.parametrize('name',
                         ['SONY ERICSSON',
                          '12345',
                          '!@#$%^&'])
def test_update_item(put_item_endpoint, item_id_fixture, name):
    assert put_item_endpoint.check_status_code_is_(200)


def test_partial_item_update(patch_item_endpoint):
    pass


def test_get_item_by_id():
    get_response = GetById()
    get_response.get_item_by_id()
    with allure.step('Check response status'):
        assert get_response.check_status_code_is_(200)


def test_delete_item_by_id(delete_item_endpoint, get_item_endpoint):
    delete_item_endpoint.delete_item_by_id(get_item_endpoint)
    assert delete_item_endpoint.check_status_code_is_(201)
