import allure
import pytest
from api_tests_yevdokiienko.tests.data import payloads


@allure.feature('hw 22')
@allure.story('Post')
def test_create_object_post(create_object_endpoint, delete_object):
    create_object_endpoint.create_object(payloads.new_object)
    delete_object.object_id = create_object_endpoint.object_id
    assert create_object_endpoint.check_status_code_is_(200)


def test_get_object_by_id(get_object_endpoint, get_object_id):
    get_object_endpoint.get_object(get_object_id)
    assert get_object_endpoint.check_status_code_is_(200)


@pytest.mark.parametrize(
    'name', ['Apple MacBook Pro 16', 'APPLE MACBOOK PRO 16']
)
@pytest.mark.parametrize(
    'year', [2019, 1990, 3050]
)
@pytest.mark.parametrize(
    'color', ['silver', 'SILVER', 'SiLvEr']
)
@pytest.mark.smoke
def test_update_object_put(
    get_object_id, session_info, put_object_endpoint, name, year, color
):
    payload = payloads.put_object
    payload['name'] = name
    payload['data']['year'] = year
    payload['data']['color'] = color
    put_object_endpoint.put_object(get_object_id, payload)
    assert put_object_endpoint.check_status_code_is_(200)
    assert put_object_endpoint.check_response_name_is_(name)
    assert put_object_endpoint.check_response_year_is_(year)
    assert put_object_endpoint.check_response_color_is_(color)


@allure.feature('hw 22')
@allure.story('Patch')
@pytest.mark.critical
def test_update_object_price(patch_object_endpoint, get_object_id):
    patch_object_endpoint.update_object(get_object_id, payloads.update_price)
    assert patch_object_endpoint.check_status_code_is_(200)
    assert patch_object_endpoint.check_response_price_is_(
        payloads.update_price['data']['price']
    )


@allure.feature('hw 22')
@allure.story('Patch')
def test_partially_update_object_patch(patch_object_endpoint, get_object_id):
    patch_object_endpoint.update_object(get_object_id, payloads.update_name)
    assert patch_object_endpoint.check_status_code_is_(200)
    assert patch_object_endpoint.check_response_name_is_(
        payloads.update_name['name']
    )


def test_delete_object(get_object_id, delete_object_endpoint):
    delete_object_endpoint.delete_object(get_object_id)
    assert delete_object_endpoint.check_status_code_is_(200)
