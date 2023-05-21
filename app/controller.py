from flask import session, jsonify
from app.models import User, Chat, ChatQuestion, ChatResponse
from app import db
from werkzeug.security import generate_password_hash

# Get the current user based on the session id
def get_user():
    user = User.query.filter_by(id=session['id']).first()
    return user

# Get the current user based on the email
def check_email(email):
    user = User.query.filter_by(email=email).first()
    return user

# Add a user to the database
def add_user(email, first_name, last_name, password):
    hashed_pw = generate_password_hash(password, method='scrypt')
    new = User(email= email, first_name = first_name, last_name = last_name, password = hashed_pw)
    db.session.add(new)
    db.session.commit()
    return new

# Update the user's information
def update_user(id, email=None, first_name=None, last_name=None):
    user = db.session.get(User, int(id))
    if user:
        if email:
            user.email = email
        if first_name:
            user.first_name = first_name
        if last_name:
            user.last_name = last_name
        db.session.commit()
        return jsonify({'success': True, 'message': 'Account updated'}), 200
    else:
        return jsonify({'success': False, 'message': 'Please try again'}), 401

# Update the user's password
def change_password(id, newpassword):
    user = db.session.get(User, int(id))
    if user:
        if newpassword:
            new_hashed_pw = generate_password_hash(newpassword, method='scrypt')
            user.password = new_hashed_pw
            db.session.commit()
            return jsonify({'success': True, 'message': 'Password updated'}), 200
        else:
            return jsonify({'success': False, 'message': 'Please try again'}), 401

# Add a chat to the database
def add_chat(user_id):
    chat = Chat(user_id=user_id)
    db.session.add(chat)
    db.session.commit()
    return chat.id

# Add a question to the database
def add_chat_question(chat_id, content, timestamp):
    chat_message = ChatQuestion(chat_id=chat_id, content=content, timestamp=timestamp)
    db.session.add(chat_message)
    db.session.commit()
    return chat_message

# Add a response to the database
def add_chat_response(chat_id, content, timestamp):
    chat_message = ChatResponse(chat_id=chat_id, content=content, timestamp=timestamp)
    db.session.add(chat_message)
    db.session.commit()
    return chat_message

# Get the user's chat ids
def get_chat_ids(user_id):
    user = User.query.filter_by(id=user_id).first()
    id_list = []
    for chat in user.chat:
        id_list.append(chat.id)
    return id_list

# Get the user's chat questions
def get_chat_questions(chat_id):
    chat = Chat.query.filter_by(id=chat_id).first()
    questions = []
    for question in chat.chat_questions:
        question = [question.content, question.timestamp]
        questions.append(question)
    return questions

# Get the user's chat responses
def get_chat_responses(chat_id):
    chat = Chat.query.filter_by(id=chat_id).first()
    responses = []
    for response in chat.chat_responses:
        response = [response.content, response.timestamp]
        responses.append(response)
    return responses

# Get the user's chat
def get_chat(chat_id):
    chat = []
    questions = get_chat_questions(chat_id)
    responses = get_chat_responses(chat_id)
    for i in range(len(questions)):
        chat.append([])
        chat[i].append(questions[i])
        chat[i].append(responses[i])
    return chat

# Get the user's chat records
def get_chat_records(user_id):
    user = User.query.filter_by(id=user_id).first()
    records = user.chat
    chat_records = []
    for chat in records:
        chat_records.append([chat.id, chat.datetime.strftime("%m/%d/%Y, %H:%M:%S")])
    return chat_records