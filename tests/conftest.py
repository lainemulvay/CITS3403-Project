import os
import pytest
from app import initapp, db
from app.models import User

@pytest.fixture(scope='module')
def test_client():
    flask_app = initapp()
    flask_app.config.from_object('config.TestingConfig')
    
    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
        yield testing_client
        with flask_app.app_context():
            db.session.remove()
            db.drop_all()

@pytest.fixture(scope='module')
def test_user_table():
    flask_app = initapp()
    flask_app.config.from_object('config.TestingConfig')

    with flask_app.app_context():
        user = User(first_name='test', last_name='user',)