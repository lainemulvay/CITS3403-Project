from app import app, db
from app.models import User, Chat, ChatQuestion, ChatResponse
from app.controller import add_chat, add_chat_question, add_chat_response, get_user
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.chat import chat_blueprint
from datetime import datetime

# chat page
@chat_blueprint.route("/chat/")
def chat():
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    username = get_user(User).first_name
    return render_template("chat_view.html", display = True, username=username)


@chat_blueprint.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))


@chat_blueprint.route('/send-text', methods=['POST'])
def save_chat():
    # Get the chat message data from the frontend
    data = request.get_json()
    questions = data['questions']
    responses = data['responses']

    user_id= session['id']
    chat_id = add_chat(user_id)

    for question in questions:
        content = question[:-22]
        timestamp = question[(len(question)-20):]
        add_chat_question(chat_id, content, timestamp)
    
    for response in responses:
        content = response[:-22]
        timestamp = response[(len(response)-20):]
        add_chat_response(chat_id, content, timestamp)

    return jsonify(success=True)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response