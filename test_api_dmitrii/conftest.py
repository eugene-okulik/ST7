import requests
import pytest
from test_api_dmitrii.tests.data import payloads
from test_api_dmitrii.endpoints.delete_post import DeletePost
from test_api_dmitrii.endpoints.post_post import PostPost
from test_api_dmitrii.endpoints.get_all_posts import GetPosts
from test_api_dmitrii.endpoints.get_post import GetPost
from test_api_dmitrii.endpoints.put_post import PutPost
from test_api_dmitrii.endpoints.patch_post import PatchPost
from test_api_dmitrii.other_checks.other_checks import SmallChecks


@pytest.fixture()
def object_id():
    print('Start testing')
    create_object = PostPost()
    create_object.create_object(payloads.payload_for_creation)
    obj_id = create_object.response_json['id']
    yield obj_id
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    print('Testing completed')


@pytest.fixture()
def follow_the_testing_without_object():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def deleted_object():
    return DeletePost()


@pytest.fixture()
def create_object():
    return PostPost()


@pytest.fixture()
def get_objects():
    return GetPosts()


@pytest.fixture()
def get_object():
    return GetPost()


@pytest.fixture()
def update_object():
    return PutPost()


@pytest.fixture()
def partially_update_object():
    return PatchPost()


@pytest.fixture()
def small_checks():
    return SmallChecks()
