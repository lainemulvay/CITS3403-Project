import os
import pytest
from app import initapp, db
from app.models import User
from werkzeug.security import generate_password_hash

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
def test_database():
    flask_app = initapp()
    flask_app.config.from_object('config.TestingConfig')

    with flask_app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()
        
@pytest.fixture(scope='module')
def test_user():
    flask_app = initapp()
    flask_app.config.from_object('config.TestingConfig')

    with flask_app.test_client() as testing_client:
        with flask_app.app_context():
            db.create_all()
            user = User(email="Test@email.com", first_name="Test", last_name="User", password="")
            user.password = generate_password_hash("Test12345%")
            db.session.add(user)
            db.session.commit()
        yield testing_client
        with flask_app.app_context():
            db.session.remove()
            db.drop_all()

