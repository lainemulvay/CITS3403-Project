import os
import pytest
from app import initapp

@pytest.fixture(scope='module')
def test_client():
    os.environ['CONFIGURATION'] = 'config.TestingConfig'
    flask_app = initapp()
    testing_client = flask_app.test_client()
    ctx = flask_app.app_context()
    ctx.push()
    yield testing_client
    ctx.pop()
    return testing_client