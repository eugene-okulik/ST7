import requests
import pytest
from pydantic import BaseModel
from typing import Any


from test_task_1 import base_url


class Publication(BaseModel):
    id: str
    name: str
    createdAt: str
    data: dict[str, Any]


def test_create_object(session_info):
    payload = {
        "name": "Apple MacBook Pro 160",
        "data": {
            "year": 2219,
            "price": 10,
            "CPU model": "Intel Core i90",
            "Hard disk size": "1 TB"
        }
    }
    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.post(
        base_url,
        json=payload,
        headers=headers
    )
    assert response.status_code == 200, 'Incorrect status code'
    Publication(**response.json())


def test_change_object_patch(object_id, session_info):
    payload = {
        "name": "Apple MacBook Pro 16 (Updated Name)"
    }
    response = requests.patch(
        url=f"{base_url}/{object_id}",
        json=payload
    )
    assert response.status_code == 200, "Status code is not 200"
    print(f'Updated patch object with id {object_id}')


@pytest.mark.skip
def test_numbers():
    assert 100 == 100