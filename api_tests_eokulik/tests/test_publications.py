import allure
from api_tests_eokulik.tests.data import payloads
from api_tests_eokulik.enpoints.post_posts import PostPosts


def test_publication_create():
    create_pub_endpoint = PostPosts()
    create_pub_endpoint.create_publication(payloads.new_pub)
    assert create_pub_endpoint.check_status_code_is_(201)
    create_pub_endpoint.check_response_title_is_(payloads.new_pub['title'])


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
