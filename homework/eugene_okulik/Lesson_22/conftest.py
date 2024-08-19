import pytest
import requests
import random


@pytest.fixture()
def publication_id():
    payload = {
        "title": "LKJHLKJDHLKJDHLKJDF",
        "body": "UYkajshdfkajdshfasdf",
        "userId": 1
    }
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer 92834756903845739845'
    }

    response = requests.post(
        'https://jsonplaceholder.typicode.com/posts',
        json=payload,
        headers=headers
    )
    # pub_id = 42
    pub_id = response.json()['id']
    # print(f'Created publication {response.json()["id"]}')
    print(f'Created publication {pub_id}')
    yield pub_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pub_id}')
    print(f'Deleted publication {pub_id}')


@pytest.fixture(scope='session')
def session_info():
    print('before')
    yield random.randrange(100, 200)
    print('after')
