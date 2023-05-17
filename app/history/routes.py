from app.controller import get_user, get_chat_ids, get_chat, get_chat_records
from flask import render_template,flash, redirect, url_for, session
# from flask_login import LoginManager, login_required, current_user, login_user
from app.history import history_blueprint

# history page
@history_blueprint.route("/history/")
def history():
    # If the user is not logged in, redirect to the login page
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    # Get the user id from the session and get the user's first name
    user_id = session['id']
    username = get_user().first_name

    # Get the chat records for the user
    chat_records = get_chat_records(user_id)
    return render_template("hist_view.html", display = True, username=username, chat_records=chat_records)

@history_blueprint.route('/logout/')
def logout():
    # Clear the session
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))

@history_blueprint.route('/history/<id>', methods=['GET'])
def view_chat_id(id):
    # If the user is not logged in, redirect to the login page
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    # If the user is logged in but the chat id is not in the user's chat ids, redirect to the history page
    elif int(id) not in get_chat_ids(session['id']):
        flash('You do not have access to this chat', 'danger')
        return redirect(url_for('history.history'))
    # Get the chat with the given id
    chat = get_chat(id)
    return render_template("base_chat.html", display = True, chat=chat)

# Disable caching for the history page
@history_blueprint.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response