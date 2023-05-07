from flask import Blueprint

register_blueprint = Blueprint('register', __name__)

from app.register import routes