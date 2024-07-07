from test_api_alex_v_project.endpoints.post_item import PostItem
from test_api_alex_v_project.tests.data import payloads


def test_create_item():
    create_item_endpoint = PostItem()
    create_item_endpoint.create_item(payloads.new_item_payload)
    assert create_item_endpoint.check_status_code_is_200(200)
    assert create_item_endpoint.check_response_title_is_(payloads.new_item_payload['name'])
