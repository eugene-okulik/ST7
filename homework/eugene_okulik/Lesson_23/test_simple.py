import pytest
import sys
import allure


@allure.feature('Simple')
@allure.story('Equals')
@pytest.mark.skipif(sys.platform == 'linux', reason='Not for linux')
@pytest.mark.regression
def test_one(session_info):
    assert 1 == 1


@allure.feature('Simple')
@allure.story('Equals')
@pytest.mark.skip(reason='Bug #123')
@pytest.mark.smoke
def test_two(session_info):
    assert 2 == 2


@allure.feature('Simple')
@allure.story('Equals')
@pytest.mark.parametrize(
    'title',
    ['klsdjfhklsjdfh', 'KJSDHKSJDDS', '29834729384', '*&^^%$^&%$'],
    ids=['small letters', 'large retters', 'numbers', 'symbols']
)
def test_threee(session_info, title):
    print('Test title is: ', title)
    assert 2 == 2


def compose(word):
    return word + 'hello'


@allure.feature('Simple')
@allure.story('Unittest')
@pytest.mark.parametrize(
    'test_word, expected_word',
    [('klsdjfhklsjdfh', 'klsdjfhklsjdfhhello'), ('KJSDHKSJDDS', 'KJSDHKSJDDShello')],
    ids=['small letters', 'large letters']
)
def test_compose(session_info, test_word, expected_word):
    # test_word, expected_word = test_pair
    result = compose(test_word)
    assert result == expected_word
