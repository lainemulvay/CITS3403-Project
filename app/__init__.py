from flask import Flask
from config import Config
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = secrets.token_urlsafe(32)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.register import register_blueprint
app.register_blueprint(register_blueprint)

from app.intro import intro_blueprint
app.register_blueprint(intro_blueprint)

from app.chat import chat_blueprint
app.register_blueprint(chat_blueprint)

from app.login import login_blueprint
app.register_blueprint(login_blueprint)

from app.history import history_blueprint
app.register_blueprint(history_blueprint)

from app.profile import profile_blueprint
app.register_blueprint(profile_blueprint)

from app import models

with app.app_context():
    db.create_all()