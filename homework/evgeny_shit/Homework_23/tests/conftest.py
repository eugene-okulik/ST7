import pytest
from homework.evgeny_shit.Homework_23.tests.fixtures import object_id, object_id_without_del


@pytest.fixture(scope='session')
def session_info():
    print('Start testing', end=' ')
    yield
    print(' Testing completed')
