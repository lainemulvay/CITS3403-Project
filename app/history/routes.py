from app import app, db
from app.models import User
from app.controller import get_user, get_chat_ids, get_chat, get_chat_records
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
    username = get_user().first_name
    chat_records = get_chat_records(user_id)
    return render_template("hist_view.html", display = True, username=username, chat_records=chat_records)

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
    elif int(id) not in get_chat_ids(session['id']):
        flash('You do not have access to this chat', 'danger')
        return redirect(url_for('history.history'))
    chat = get_chat(id)
    return render_template("base_chat.html", display = True, chat=chat)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response