from app import app, db
from app.models import User
from app.controller import get_user, get_chat_ids
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.view_chat import view_chat_blueprint

@view_chat_blueprint.route("/view_chat/")
def view_chat():
    return 1
