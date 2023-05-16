from app.models import User
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.intro import intro_blueprint

# intro page
@intro_blueprint.route("/")
def index():
    return render_template("intro_view.html")