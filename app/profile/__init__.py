from flask import Blueprint

profile_blueprint = Blueprint('profile', __name__)

from app.profile import routes