import allure

from test_api_alex_v_project.endpoints.post_item import PostItem
from test_api_alex_v_project.tests.data import payloads
from test_api_alex_v_project.endpoints.get_item import GetById


def test_create_item():
    create_item_endpoint = PostItem()
    create_item_endpoint.create_item(payloads.new_item_payload)
    assert create_item_endpoint.check_status_code_is_200(200)
    assert create_item_endpoint.check_response_title_is_(payloads.new_item_payload['name'])


def test_get_item_by_id(get_item_endpoint):
    get_item_endpoint.get_item_by_id()
    with allure.step('Check response status'):
        assert get_item_endpoint.check_status_code_is_200(200)
