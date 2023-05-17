from app import initapp

app = initapp()

def test_index_page():
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"UWA FAQ Chat System" in response.data
        assert b"Get Started" in response.data
        assert b"FAQ" in response.data
        assert b"Prompt Responses" in response.data
        assert b"History" in response.data

def test_login_page():
    """
    GIVEN a Flask application
    WHEN the '/login' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/login/')
        assert response.status_code == 200
        assert b"UWA FAQ Chat System" in response.data
        assert b"Sign into your account" in response.data
        assert b"Email Address" in response.data
        assert b"Password" in response.data
        assert b"Sign in" in response.data
        assert b"Back" in response.data
        assert b"Register here" in response.data

def test_register_page():
    """
    GIVEN a Flask application
    WHEN the '/register' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/register/')
        assert response.status_code == 200
        assert b"UWA FAQ Chat System" in response.data
        assert b"Register a new account" in response.data
        assert b"First Name" in response.data
        assert b"Last Name" in response.data
        assert b"Email Address" in response.data
        assert b"Enter a new Password" in response.data
        assert b"Confirm password" in response.data
        assert b"Register" in response.data
        assert b"Back" in response.data
        assert b"Already have an account?" in response.data