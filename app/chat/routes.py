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

    if request.method == 'POST':
        
        user_message = request.form['user_message']

        # call chatbot API ******** still trying to integrate this ********
        chatbot_response = requests.get('http://mychatbotapi.com', params={'user_message': user_message}).text

        # create new chat and chat response instances
        user_id = User.query.filter_by(email=session['email']).first().id
        chat = Chat(user_id=user_id, text=user_message, created_at=datetime.utcnow())
        chat_response = ChatResponse(chat_id=chat.id, text=chatbot_response, created_at=datetime.utcnow())

        # add new instances to the database
        db.session.add(chat)
        db.session.add(chat_response)
        db.session.commit()
    return render_template("chat_view.html", display = True)


@chat_blueprint.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))