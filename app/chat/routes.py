from app import app, db
from app.models import User
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.chat import chat_blueprint

# chat page
@chat_blueprint.route("/chat/")
def chat():
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login'))
    return render_template("chat_view.html", display = True)


@chat_blueprint.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))