from flask import url_for
from app.models import User, Chat, ChatMessage
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.exc import SQLAlchemyError
import sys
from datetime import datetime

def add_chat(user_id):
    chat = Chat(user_id=user_id)
    db.session.add(chat)
    db.session.commit()
    return chat.id

def add_chat_message(chat_id, question, response):
    chat_message = ChatMessage(chat_id=chat_id, question=question, response=response)
    db.session.add(chat_message)
    db.session.commit()
    return chat_message