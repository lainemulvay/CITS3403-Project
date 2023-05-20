from flask import Flask
import secrets
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()

def initapp(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.secret_key = secrets.token_urlsafe(32)
    db.init_app(app)
    migrate.init_app(app, db)
    with app.app_context():
        print("Creating database tables...")
        db.create_all()

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

    return app

from app import models