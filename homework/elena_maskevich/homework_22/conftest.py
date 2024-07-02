import requests
import pytest
import random
from pydantic import BaseModel
from typing import Any

from test_task_1 import base_url


@pytest.fixture(scope='session')
def session_info():
    print('Start testing')
    yield random.randrange(100, 200)
    print('Testing completed')


@pytest.fixture()
def object_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
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
    obj_id = response.json()['id']
    print(f'Created object id {response.json()["id"]}')
    yield obj_id
    requests.delete(f'{base_url}/{obj_id}')
    print(f'Deleted object id {obj_id}')
