import pytest
import requests
from test_api_kate.endpoints.ob_put_update import ObPutUpdate
from test_api_kate.endpoints.ob_patch_update import ObPatchUpdate
from test_api_kate.endpoints.ob_deleted import ObDeleted


@pytest.fixture()
def new_object():
    payload = {
        "name": "Apple MacBook Pro Kate",
        "data": {
            "year": 2025,
            "price": 2849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(
        'https://api.restful-api.dev/objects',
        json=payload,
        headers=headers
    )
    new_object_id = response.json()["id"]
    print(f'Created object {new_object_id}')
    yield new_object_id
    requests.delete(f'https://api.restful-api.dev/objects/{new_object_id}')
    print(f'Deleted object {new_object_id}')


@pytest.fixture()
def updated_with_put():
    return ObPutUpdate()


@pytest.fixture()
def updated_with_patch():
    return ObPatchUpdate()
