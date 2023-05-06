'''tests the flask application for authentifycation and registration. 
ensuring the response from the user is unique and verifyable in the database'''


from datetime import datetime, timedelta
import unittest, os
from application import app, db
from application.models import Animals, Users, Attempts
from config import basedir

class ModelsTest(unittest.TestCase):
	#creates a test database that is not the real database
    def setUp(self):
        # basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] =\
            'sqlite:///' + os.path.join(basedir, 'test.db')
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.app = app.test_client()
        db.create_all()
#tearDown: removes any data whcih was added to the test database during the test, dropping them all
    def tearDown(self):
        db.session.remove()
        db.session.commit()
        db.drop_all()
#tests whether the app can properly validate a users password
    def test_password_hashing(self):
        u = Users(username='Tim')
        u.set_password('cits3403isfun')
        self.assertFalse(u.check_password('cits3403sucks'))
        self.assertTrue(u.check_password('cits3403isfun'))
#function to simulate login for testing purposes
    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)
#a test in the case that the login info doesnt match anything in the DB
    def test_incorrect_login(self):
        u = Users(username = 'testcase', email = 'test@example.com')
        u.set_password('TEST')
        db.session.add(u)
        db.session.commit()
        response = self.login('testcase','wrongpassword')
        self.assertIn(b'Invalid username or password', response.data)
#tests the case of when the login info is correct
    def test_correct_login(self):
        u = Users(username = 'testcase', email = 'test@example.com')
        u.set_password('correctpassword')
        db.session.add(u)
        db.session.commit()
        self.login('testcase','correctpassword')
        login = self.app.get('/',follow_redirects=True)
        
        ### gamepage - associated page for chat_view
        
        self.assertIn(login.data, self.app.get('/gamepage').data)
#function to simulate registering for testing purposes
    def register(self, username, email, password, password2):
        return self.app.post('/register', data=dict(
            username=username,
            email=email,
            password=password,
            password2=password2
        ), follow_redirects=True)
#tests once the user successfully registers their account
    def test_registration(self):
        response = self.register('iexist', 'iexist@example.com','pwd','pwd')
        self.assertIn(b'Thankyou for Registering!', response.data)
#test if a user tries to register with a username already in database
    def test_register_non_unique_user(self):
        u1 = Users(username="iexist", email='iexist@example.com')
        db.session.add(u1)
        db.session.commit()
        register = self.register('iexist', 'different@example.com','pwd','pwd')
        self.assertIn(b'Please use a different username.', register.data)
#test if a user tries to register with an email already in database
    def test_register_non_unique_email(self):
        u1 = Users(username="iexist", email='iexist@example.com')
        db.session.add(u1)
        db.session.commit()
        register = self.register('iwanttoexist', 'iexist@example.com','pwd','pwd')
        self.assertIn(b'Please use a different email address.', register.data)

if __name__ == '__main__':
    unittest.main(verbosity=2)