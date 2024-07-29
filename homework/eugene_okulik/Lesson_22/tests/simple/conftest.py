import pytest
import random


@pytest.fixture(scope='session')
def session_info():
    print('before SIMPLE')
    yield random.randrange(100, 200)
    print('after SIMPLE')
