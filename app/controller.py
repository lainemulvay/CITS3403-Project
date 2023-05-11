from flask import url_for
from app.model import User, Chat, ChatMessage
from app import db
from flask_login import current_user, login_user, logout_user
from sqlalchemy.orm.attributes import flag_modified
from sqlalchemy.exc import SQLAlchemyError
import sys
from datetime import datetime

def add_chat(user_id):
    chat = Chat(user_id=user_id, )
    db.session.add(chat)
    db.session.commit()
    return chat