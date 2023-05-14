from flask import url_for, session
from app.models import User, Chat, ChatQuestion, ChatResponse
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.exc import SQLAlchemyError
import sys
from datetime import datetime

def get_user(user):
    user = User.query.filter_by(id=session['id']).first()
    return user

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