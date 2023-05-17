import os
import pytest
from app import initapp

@pytest.fixture(scope='module')
def test_client():
    os.environ['CONFIGURATION'] = 'config.TestingConfig'
    flask_app = initapp()
    
    with flask_app.test_client() as testing_client:
        yield testing_client