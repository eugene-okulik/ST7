import pytest
import requests
from api_tests_eokulik.enpoints.get_by_id import GetById
from api_tests_eokulik.enpoints.post_posts import PostPosts
from api_tests_eokulik.tests.data import payloads
from _pytest.fixtures import SubRequest


@pytest.fixture()
def publication_id(create_pub_endpoint):
    create_pub_endpoint.create_publication(payloads.new_pub)
    pub_id = create_pub_endpoint.response_json['id']
    yield pub_id
    requests.delete(f'https://jsonplaceholder.typicode.com/posts/{pub_id}')
    print(f'Deleted publication {pub_id}')


@pytest.fixture()
def delete_after_test(request: SubRequest):
    request.obj_id = None
    yield request
    print(f'I will delete obj wit id {request.obj_id}')

@pytest.fixture()
def get_pub_endpoint():
    return GetById()


@pytest.fixture()
def create_pub_endpoint():
    return PostPosts()
