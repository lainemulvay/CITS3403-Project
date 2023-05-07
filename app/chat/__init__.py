from flask import Blueprint

chat_blueprint = Blueprint('chat', __name__)

from app.chat import routes