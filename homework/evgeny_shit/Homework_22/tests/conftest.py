import pytest
from .fixtures import object_id, object_id_without_del


@pytest.fixture(scope='session')
def session_info():
    print('Start testing', end=' ')
    yield
    print(' Testing completed')
