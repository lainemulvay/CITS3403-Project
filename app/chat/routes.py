from app import app, db
from app.models import Chat, ChatMessage, User
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
    return render_template("chat_view.html", display = True)


@chat_blueprint.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))


@chat_blueprint.route('/send_text', methods=['POST'])
def save_chat():
    # Get the chat message data from the frontend
    data = request.get_json()
    input = data['input']
    print(input[0])
    print()
    response = data['response']
    print(response[0])
    return 'Text received'

    # chat_id = data.get('chat_id')
    # question = data.get('question')
    # response = data.get('response')
    # # Create a new chat message
    # chat_message = ChatMessage(chat_id=chat_id, question=question, response=response)
    
    # # Add the chat message to the database
    # db.session.add(chat_message)
    # db.session.commit()

    return jsonify(success=True)

'''
def save_chat():
    data = request.json
    print(data)
    return
'''