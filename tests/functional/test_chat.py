import json

def test_index_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response contains the index page content
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
    THEN check the response contains the login page content
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
    THEN check the response contains the correct content
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
    THEN check the response redirects to the login page
    """
    response = test_client.get('/chat/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_invalid_history_access(test_client):
    """
    GIVEN a Flask application
    WHEN the '/history' page is requested (GET), and the user is not logged in
    THEN check the response redirects to the login page
    """
    response = test_client.get('/history/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_invalid_chat_id_access(test_client):
    """
    GIVEN a Flask application
    WHEN the '/history/<id>' page is requested (GET), and the user is not logged in
    THEN check the response redirects to the login page
    """
    response = test_client.get('/history/1')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_invalid_profile_access(test_client):
    """
    GIVEN a Flask application
    WHEN the '/profile' page is requested (GET), and the user is not logged in
    THEN check the response redirects to the login page
    """
    response = test_client.get('/profile/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_register(test_client):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to (POST)
    THEN check the user is registered
    """
    response = test_client.post('/register/', data=dict(
        firstname="Test",
        lastname="Test",
        email="Test@email.com",
        newpw="Test12345%",
        confirmpw="Test12345%",
    ))
    assert b"Account successfully created" in response.data

def test_duplicate_register(test_client):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to (POST) with a duplicate email
    THEN check user is not registered
    """
    response = test_client.post('/register/', data=dict(
        firstname="Test",
        lastname="Test",
        email="Test@email.com",
        newpw="Test12345%",
        confirmpw="Test12345%",
    ))
    assert b"Email already exists" in response.data

def test_invalid_login_email(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST) with invalid email
    THEN check login fails
    """
    response = test_client.post('/login/', data=dict(
        email="",
        password="",
    ))
    assert b"Invalid email" in response.data

def test_invalid_login_password(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST) with invalid password
    THEN check login fails
    """
    response = test_client.post('/login/', data=dict(
        email="Test@email.com",
        password="",
    ))
    assert b"Invalid password" in response.data

def test_not_logged_user_info(test_client):
    """
    GIVEN a Flask application
    WHEN the '/me' page is requested (GET) and user is not logged in
    THEN check the response contains not logged in message
    """
    response = test_client.get('/me/')
    assert response.status_code == 200
    assert b"User not logged in" in response.data

def test_login(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is posted to (POST) with valid credentials
    THEN check the user is logged in
    """
    response = test_client.post('/login/', data=dict(
        email="Test@email.com",
        password="Test12345%",
    ))
    assert b"Login success" in response.data

def test_logged_user_info(test_client):
    """
    GIVEN a Flask application
    WHEN the '/me' page is requested (GET) and user is logged in
    THEN check the response contains user info with lowercase email
    """
    response = test_client.get('/me/')
    assert response.status_code == 200
    assert b"1" in response.data
    assert b"test@email.com" in response.data
    assert b"Test" in response.data

def test_auto_log_in(test_client):
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET) and user is logged in already
    THEN redirect to '/chat'
    """
    response = test_client.get('/login/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data
    
def test_chat_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/chat' page is requested (GET)
    THEN check the response contains the chat page
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

def test_save_chat(test_client):
    """
    GIVEN a Flask application
    WHEN the '/chat' page is posted to (POST) with valid data
    THEN check the chat is saved
    """
    headers = {
        'Content-Type': 'application/json'
    }
    questions = ["question1 5/18/2023, 10:44:58 PM", "question2 5/18/2023, 10:44:58 PM", "question3 5/18/2023, 10:44:58 PM"]
    responses = ["response1 5/18/2023, 10:44:58 PM", "response2 5/18/2023, 10:44:58 PM", "response3 5/18/2023, 10:44:58 PM"]
    data = json.dumps({"questions": questions, "responses": responses})
    response = test_client.post('/send-text/', data = data, headers = headers)

    assert b"Chat successfully saved" in response.data


def test_history_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/history' page is requested (GET)
    THEN check the response contains the history page
    """
    response = test_client.get('/history/')
    assert response.status_code == 200
    assert b"Chat History" in response.data
    assert b"Chat" in response.data
    assert b"History" in response.data
    assert b"My Account" in response.data
    assert b"Logout" in response.data

def test_view_history(test_client):
    """
    GIVEN a Flask application
    WHEN the '/history' page is requested (GET)
    THEN check the response contains chat history
    """
    response = test_client.get('/history/1')
    assert response.status_code == 200
    assert b"question1" in response.data
    assert b"response1" in response.data

def test_profile_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/account' page is requested (GET)
    THEN check the response contains user info
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
    assert b"test@email.com" in response.data
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
    WHEN the '/account' page is posted to (POST) and user changed account information
    THEN check the account is updated
    """
    response = test_client.post('/profile/', data=dict(
        action = "update_account",
        firstname="Change",
        lastname="Change",
        email="Change@email.com",
    ))

    assert b"Account updated" in response.data

def test_invalid_old_password(test_client):
    """
    GIVEN a Flask application
    WHEN the '/account' page is posted to (POST) and user changed password with invalid old password
    THEN check the password is not updated
    """
    response = test_client.post('/profile/', data=dict(
        action = "update_password",
        oldpw="",
        newpw="Change12345%",
    ))

    assert b"Existing password is not correct, please try again" in response.data

def test_change_password(test_client):
    """
    GIVEN a Flask application
    WHEN the '/account' page is posted to (POST) and user changed password with valid old password
    THEN check the password is updated
    """
    response = test_client.post('/profile/', data=dict(
        action = "update_password",
        oldpw="Test12345%",
        newpw="Change12345%",
    ))

    assert b"Password updated" in response.data

def test_logout(test_client):
    """
    GIVEN a Flask application
    WHEN the '/logout' page is requested (GET)
    THEN check the user is redirected to login page
    """
    response = test_client.get('/logout/')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data

def test_invalid_chat_id_access_from_logged_in_user(test_client):
    """
    GIVEN a Flask application
    WHEN the '/history/<id>' page is requested (GET) with invalid user id
    THEN check the user is redirected to history page
    """
    test_client.post('/register/', data=dict(
        firstname="Test2",
        lastname="Test2",
        email="Test2@email.com",
        newpw="Test12345%",
        confirmpw="Test12345%",
    ))

    test_client.post('/login/', data=dict(
        email="Test2@email.com",
        password="Test12345%",
    ))

    response = test_client.get('/history/1')
    assert response.status_code == 302
    assert b"Redirecting..." in response.data