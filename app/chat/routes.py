from app.controller import add_chat, add_chat_question, add_chat_response, get_user
from flask import render_template,flash, redirect, url_for, session, request, jsonify
from app.chat import chat_blueprint

# chat page
@chat_blueprint.route("/chat/")
def chat():
    # If the user is not logged in, redirect to the login page
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    username = get_user().first_name
    return render_template("chat_view.html", display = True, username=username)


@chat_blueprint.route('/logout/')
def logout():
    # Clear the session
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))


@chat_blueprint.route('/send-text/', methods=['POST'])
def save_chat():
    # Get the chat message data from the frontend
    data = request.get_json()
    questions = data['questions']
    print(questions[0])
    responses = data['responses']

    # Get the user id from the session and add chat to the database
    user_id= session['id']
    chat_id = add_chat(user_id)

    for question in questions:
        content = question[:-23]
        timestamp = question[(len(question)-23):]
        add_chat_question(chat_id, content, timestamp)
    
    for response in responses:
        content = response[:-23]
        timestamp = response[(len(response)-23):]
        add_chat_response(chat_id, content, timestamp)

    return jsonify({"success" : True, 'message': "Chat successfully saved"}), 200

# Disable caching for the chat page
@chat_blueprint.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response