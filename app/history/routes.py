from app import app, db
from app.models import User
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
    return render_template("hist_view.html", display = True)

@history_blueprint.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login.login'))

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response