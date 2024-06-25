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
    print(f'Created publication {response.json()["id"]}')
    # print(f'Created publication {pub_id}')
    yield pub_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pub_id}')
    print(f'Deleted publication {pub_id}')


@pytest.fixture(scope='session')
def session_info():
    print('before')
    yield random.randrange(100, 200)
    print('after')


@pytest.mark.smoke
def test_get_all(session_info):
    print(session_info)
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert response.json()[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'


@pytest.mark.regression
@pytest.mark.smoke
def test_update_with_put(publication_id, session_info):
    print(session_info)
    payload = {
        "title": "LKJHLKJDHLKJDHLKJDF-UPD",
        "body": "UYkajshdfkajdshfasdf-UPD",
        "userId": 1
    }

    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{publication_id}',
        json=payload
    )
    print(f'Updated publication {publication_id}')
    assert response.json()['title'] == payload['title']


@pytest.mark.regression
def test_one():
    assert 1 == 1


@pytest.mark.smoke
def test_two():
    assert 2 == 2
