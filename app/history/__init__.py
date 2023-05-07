from flask import Blueprint

history_blueprint = Blueprint('history', __name__)

from app.history import routes