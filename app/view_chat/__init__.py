from flask import Blueprint

view_chat_blueprint = Blueprint('view_chat', __name__)

from app.view_chat import routes