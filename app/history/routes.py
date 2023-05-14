from app import app, db
from app.models import User
from app.controller import get_user, get_chat_ids, get_chat
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.history import history_blueprint

# history page
@history_blueprint.route("/history/")
def history():
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    user_id = session['id']
    id_list = get_chat_ids(user_id)
    username = get_user(User).first_name
    return render_template("hist_view.html", display = True, username=username, ids=id_list)

@history_blueprint.route('/logout/')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))

@history_blueprint.route('/history/<id>', methods=['GET'])
def view_chat_id(id):
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    chat_id = id
    chat = get_chat(chat_id)
    return render_template("base_chat.html", display = True, chat=chat, id=chat_id)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response