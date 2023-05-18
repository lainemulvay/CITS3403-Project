from app.controller import *
from app.models import *
from app import initapp

app = initapp()

def test_add_user(test_database):
    """
    GIVEN a User model
    WHEN a new User is added
    THEN check the email, first_name, last_name are defined correctly
    and password is hashed
    """
    add_user("Test@email.com", "Test", "Test", "Test12345%")
    user = User.query.filter_by(email="Test@email.com").first()

    assert user.email == 'Test@email.com'
    assert user.first_name == 'Test'
    assert user.last_name == 'Test'
    assert user.password != 'Test12345%'

def test_get_user(test_database):
    user = check_email('Test@email.com')
    assert user.email == 'Test@email.com'

def test_update_user(test_database):
    """
    GIVEN a User model
    WHEN an existing user is updated
    THEN information is updated
    """
    user = User.query.filter_by(id=1).first()
    old_email = user.email
    old_first_name = user.first_name
    update_user(1, "Change@email.com", "Change", "Change")
    updated_user = User.query.filter_by(id=1).first()

    assert old_email == 'Test@email.com'
    assert old_first_name == 'Test'
    assert updated_user.email == "Change@email.com"
    assert updated_user.first_name == "Change"

def test_change_password(test_database):
    """
    GIVEN a User model
    WHEN an existing user's password is changed
    THEN the password is updated
    """
    user = User.query.filter_by(id=1).first()
    old_password = user.password
    change_password(1, "ChangePassword12345%")
    updated_user = User.query.filter_by(id=1).first()

    assert old_password != updated_user.password

def test_add_chat(test_database):
    """
    GIVEN a Chat model
    WHEN a new chat is added
    THEN check the user_id is defined correctly
    """
    chat_id = add_chat(1)
    chat = Chat.query.filter_by(id=chat_id).first()

    assert chat.user.id == 1

def test_add_chat_question(test_database):
    """
    GIVEN a ChatQuestion model
    WHEN a new question is added
    THEN check the chat_id, content, and timestamp are defined correctly
    """
  
    chat_message = add_chat_question(1, "question", "2021-04-01 00:00:00")
    chat_question = ChatQuestion.query.filter_by(id=chat_message.id).first()

    assert chat_question.chat.id == 1
    assert chat_question.content == "question"
    assert chat_question.timestamp == "2021-04-01 00:00:00"

def test_add_chat_response(test_database):
    """
    GIVEN a ChatResponse model
    WHEN a new response is added
    THEN check the chat_id, content, and timestamp are defined correctly
    """
    chat_message = add_chat_response(1, "response", "2021-04-01 00:00:00")
    chat_response = ChatResponse.query.filter_by(id=chat_message.id).first()

    assert chat_response.chat.id == 1
    assert chat_response.content == "response"
    assert chat_response.timestamp == "2021-04-01 00:00:00"

def test_get_chat_ids(test_database):
    """
    GIVEN a Chat model
    WHEN a new chat is added
    THEN check the chat_id is returned
    """
    chat_ids = get_chat_ids(1)

    assert 1 in chat_ids

def test_get_chat_questions(test_database):
    """
    GIVEN a ChatQuestion model
    WHEN a new question is added
    THEN check the chat_id, content, and timestamp are returned
    """
    chat_questions = get_chat_questions(1)

    assert chat_questions[0][0] == "question"
    assert chat_questions[0][1] == "2021-04-01 00:00:00"

def test_get_chat_responses(test_database):
    """
    GIVEN a ChatResponse model
    WHEN a new response is added
    THEN check the chat_id, content, and timestamp are returned
    """
    chat_responses = get_chat_responses(1)

    assert chat_responses[0][0] == "response"
    assert chat_responses[0][1] == "2021-04-01 00:00:00"

def test_get_chat(test_database):
    """
    GIVEN a Chat model
    WHEN a new chat is added
    THEN check the chat_id is returned
    """
    chat = get_chat(1)

    assert chat[0][0][0] == "question"
    assert chat[0][0][1] == "2021-04-01 00:00:00"
    assert chat[0][1][0] == "response"
    assert chat[0][1][1] == "2021-04-01 00:00:00"

def test_get_chat_records(test_database):
    """
    GIVEN a Chat model
    WHEN a new chat is added
    THEN check the chat_id is returned
    """
    chat_records = get_chat_records(1)

    assert chat_records[0][0] == 1
    #Can't test timestamp because it is generated based on current time