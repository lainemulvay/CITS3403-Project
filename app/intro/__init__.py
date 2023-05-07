from flask import Blueprint

intro_blueprint = Blueprint('intro', __name__)

from app.intro import routes