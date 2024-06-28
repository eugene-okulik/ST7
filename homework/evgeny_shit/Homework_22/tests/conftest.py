from .fixtures import *


@pytest.fixture(scope='session')
def session_info():
    print('Start testing', end=' ')
    yield
    print(' Testing completed')
