import allure
import pytest


@allure.description('Check skipping test')
@allure.feature('Simple test')
@allure.story('Equals')
@allure.title('Skipping test')
@pytest.mark.skip(reason='Teacher said')
def test_to_skip(follow_the_testing_without_object):
    with allure.step('Check equals'):
        assert 2 == 2


@allure.description('Check failing test')
@allure.feature('Simple test')
@allure.story('Equals')
@allure.title('Failing test')
@pytest.mark.smoke
def test_to_failing(follow_the_testing_without_object):
    with allure.step('Check equals'):
        assert 2 != 2
