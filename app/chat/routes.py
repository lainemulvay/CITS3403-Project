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
        return redirect(url_for('login'))
    return render_template("chat_view.html", display = True)


@chat_blueprint.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))


@chat_blueprint.route('/send_text', methods=['POST'])
def save_chat():
    data = request.json
    user = User.query.filter_by(email=session['email']).first()
    if user:
        chat = Chat(user_id=user.id, date=datetime.utcnow())
        db.session.add(chat)
        db.session.commit()
        chat_id = chat.id
        messages = []
        for message in data['messages']:
            chat_message = ChatMessage(chat_id=chat_id, question=message['question'], response=message['response'])
            db.session.add(chat_message)
            messages.append(chat_message)
        db.session.commit()
        response_data = {'success': True, 'messages': messages}
    else:
        response_data = {'success': False, 'error': 'User not found.'}
    return jsonify(response_data)

'''
def save_chat():
    data = request.json
    print(data)
    return
'''