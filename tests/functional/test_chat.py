from app import initapp
from app import db

app = initapp()

def test_index_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"UWA FAQ Chat System" in response.data
    assert b"Get Started" in response.data
    assert b"FAQ" in response.data
    assert b"Prompt Responses" in response.data
    assert b"History" in response.data

def test_login_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """

    response = test_client.get('/login/')
    assert response.status_code == 200
    assert b"UWA FAQ Chat System" in response.data
    assert b"Sign into your account" in response.data
    assert b"Email Address" in response.data
    assert b"Password" in response.data
    assert b"Sign in" in response.data
    assert b"Back" in response.data
    assert b"Register here" in response.data

def test_register_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/register' page is requested (GET)
    THEN check the response is valid
    """
    
    response = test_client.get('/register/')
    assert response.status_code == 200
    assert b"Register a new account" in response.data
    assert b"First name" in response.data
    assert b"Last name" in response.data
    assert b"Email address" in response.data
    assert b"Enter a new password" in response.data
    assert b"Confirm password" in response.data
    assert b"Register" in response.data
    assert b"Back" in response.data

def test_invalid_chat_access(test_client):
    """
    GIVEN a Flask application
    WHEN the '/chat' page is requested (GET), and the user is not logged in
    THEN check the response is valid
    """
    response = test_client.get('/chat/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_invalid_history_access(test_client):
    """
    GIVEN a Flask application
    WHEN the '/history' page is requested (GET), and the user is not logged in
    THEN check the response is valid
    """
    response = test_client.get('/history/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_register(test_client):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/register/', data=dict(
        firstname="Test",
        lastname="Test",
        email="Test@email.com",
        newPW="Test12345%",
        confirmPW="Test12345%",
    ))
    assert b"Account successfully created" in response.data

def test_duplicate_register(test_client):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/register/', data=dict(
        firstname="Test",
        lastname="Test",
        email="Test@email.com",
        newPW="Test12345%",
        confirmPW="Test12345%",
    ))
    assert b"Email already exists" in response.data

def test_invalid_login_email(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login/', data=dict(
        email="",
        password="",
    ))
    assert b"Invalid email" in response.data

def test_invalid_login_password(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login/', data=dict(
        email="Test@email.com",
        password="",
    ))
    assert b"Invalid password" in response.data

def test_login(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/login/', data=dict(
        email="Test@email.com",
        password="Test12345%",
    ))
    assert b"Login success" in response.data

def test_logged_user_info(test_client):
    """
    GIVEN a Flask application
    WHEN the '/me' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/me/')
    assert response.status_code == 200
    assert b"1" in response.data
    assert b"test@email.com" in response.data
    assert b"Test" in response.data

def test_chat_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/chat' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/chat/')
    assert response.status_code == 200
    assert b"Welcome to UWA's FAQ Chat Service!" in response.data
    assert b"Save Chat" in response.data
    assert b"Ask me a question..." in response.data
    assert b"Send" in response.data
    assert b"Chat" in response.data
    assert b"History" in response.data
    assert b"My Account" in response.data
    assert b"Logout" in response.data

def test_history_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/history' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/history/')
    assert response.status_code == 200
    assert b"Chat History" in response.data
    assert b"Chat" in response.data
    assert b"History" in response.data
    assert b"My Account" in response.data
    assert b"Logout" in response.data

def test_profile_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/account' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/profile/')
    assert response.status_code == 200
    assert b"My Account" in response.data
    assert b"Account Information" in response.data
    assert b"Password Setting" in response.data
    assert b"First Name" in response.data
    assert b"Last Name" in response.data
    assert b"Test" in response.data
    assert b"Email" in response.data
    assert b"Password Setting" in response.data
    assert b"Existing Password" in response.data
    assert b"New Password" in response.data
    assert b"Confirm New Password" in response.data
    assert b"Update Password" in response.data

    assert b"Chat" in response.data
    assert b"History" in response.data
    assert b"My Account" in response.data
    assert b"Logout" in response.data

def test_change_account_information(test_client):
    """
    GIVEN a Flask application
    WHEN the '/account' page is posted to (POST)
    THEN check the response is valid
    """
    response = test_client.post('/profile/', data=dict(
        action = "update_account",
        firstname="Change",
        lastname="Change",
        email="Change@email.com",
    ))

    assert b"Account updated" in response.data

def test_logout(test_client):
    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/logout/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data