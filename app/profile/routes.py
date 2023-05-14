from app import app, db
from app.models import User
from app.controller import get_user
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.profile import profile_blueprint

@profile_blueprint.route("/profile/")
def profile():
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    firstname = get_user(User).first_name
    lastname = get_user(User).last_name
    email = get_user(User).email
    # return user details
    return render_template("profile_view.html", display = True, username=firstname, firstname=firstname, lastname=lastname, email=email)