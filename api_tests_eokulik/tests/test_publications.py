import allure
from api_tests_eokulik.tests.data import payloads
from api_tests_eokulik.enpoints.post_posts import PostPosts
from api_tests_eokulik.utils.delete_pub import del_pub


def test_publication_create(delete_after_test):
    create_pub_endpoint = PostPosts()
    delete_after_test.obj_id = create_pub_endpoint.create_publication(payloads.new_pub)
    # delete_publication.obj_id = create_pub_endpoint.obj_id
    # obj_id = create_pub_endpoint.obj_id
    assert create_pub_endpoint.check_status_code_is_(201)
    create_pub_endpoint.check_response_title_is_(payloads.new_pub['title'])
    # del_pub(obj_id)


@allure.description('This test checks getting a publication by its Id')
@allure.feature('Publications')
@allure.story('Get')
def test_by_id(get_pub_endpoint):
    get_pub_endpoint.get_publication(42)
    assert get_pub_endpoint.check_status_code_is_(200)
    # with allure.step('Check response status'):
    #     assert response.status_code == 200
    # with allure.step('Check response schema'):
    #     Publication(**response.json())
