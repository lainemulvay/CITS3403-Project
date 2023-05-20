from app.models import User

def test_get_password():
    """
    GIVEN a User model
    WHEN a user's password is retrieved
    THEN the password is returned
    """

    user = User("Test@email.com", "Test", "Test", "Test12345%")
    
    assert user.get_password() == "Test12345%"