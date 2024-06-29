import pytest
import requests


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
    pub_id = 42
    yield pub_id
    requests.delete('https://jsonplaceholder.typicode.com/posts/42')


@pytest.fixture()
def before_after_greetings():
    print('Start testing')
    yield
    print('Testing completed')


def test_get_publication(publication_id, before_after_greetings):
    requests.get(f'https://jsonplaceholder.typicode.com/posts/{publication_id}')
    assert publication_id == 42


@pytest.mark.smoke
def test_get_all():
    response = requests.request('GET', 'https://jsonplaceholder.typicode.com/posts')
    assert response.status_code == 200
    assert response.json()[0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'


def test_update(publication_id):
    payload = {
        "title": "LKJHLKJDHLKJDHLKJDF-UPD-test",
        "body": "UYkajshdfkajdshfasdf-UPF-test",
        "userId": 1
    }

    response = requests.put(
        f'https://jsonplaceholder.typicode.com/posts/{publication_id}',
        json=payload
    )
    assert response.json()['title'] == payload['title']


@pytest.mark.regression
def test_delete(publication_id):
    payload = {
        "title": "LKJHLKJDHLKJDHLKJDF-UPD-test",
        "body": "UYkajshdfkajdshfasdf-UPF-test",
        "userId": 1
    }

    response = requests.delete(
        f'https://jsonplaceholder.typicode.com/posts/{publication_id}',
        json=payload
    )
    assert response.status_code == 200, 'Opps!?! publication vanishing has not been done yet'
