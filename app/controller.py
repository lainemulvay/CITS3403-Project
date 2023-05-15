from flask import url_for, session, request, jsonify
from app.models import User, Chat, ChatQuestion, ChatResponse
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.exc import SQLAlchemyError
import sys
from datetime import datetime

def get_user():
    user = User.query.filter_by(id=session['id']).first()
    return user

def check_email():
    user = User.query.filter_by(email=request.form["email"].lower()).first()
    return user

def add_user(email, first_name, last_name, hashed_pw):
    new = User(email= email, first_name = first_name, last_name = last_name, password = hashed_pw)
    db.session.add(new)
    db.session.commit()
    return new

def update_user(id, email=None, first_name=None, last_name=None):
    user = User.query.get(id)
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

def add_chat(user_id):
    chat = Chat(user_id=user_id)
    db.session.add(chat)
    db.session.commit()
    return chat.id

def add_chat_question(chat_id, content, timestamp):
    chat_message = ChatQuestion(chat_id=chat_id, content=content, timestamp=timestamp)
    db.session.add(chat_message)
    db.session.commit()
    return chat_message

def add_chat_response(chat_id, content, timestamp):
    chat_message = ChatResponse(chat_id=chat_id, content=content, timestamp=timestamp)
    db.session.add(chat_message)
    db.session.commit()
    return chat_message

def get_chat_ids(user_id):
    user = User.query.filter_by(id=user_id).first()
    id_list = []
    for chat in user.chat:
        id_list.append(chat.id)
    return id_list

def get_chat_questions(chat_id):
    chat = Chat.query.filter_by(id=chat_id).first()
    questions = []
    for question in chat.chat_questions:
        question = [question.content, question.timestamp]
        questions.append(question)
    return questions

def get_chat_responses(chat_id):
    chat = Chat.query.filter_by(id=chat_id).first()
    responses = []
    for response in chat.chat_responses:
        response = [response.content, response.timestamp]
        responses.append(response)
    return responses

def get_chat(chat_id):
    chat = []
    questions = get_chat_questions(chat_id)
    responses = get_chat_responses(chat_id)
    for i in range(len(questions)):
        chat.append([])
        chat[i].append(questions[i])
        chat[i].append(responses[i])
    return chat