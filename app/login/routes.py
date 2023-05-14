from app import app, db
from app.models import User
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.login import login_blueprint

# login function
@login_blueprint.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check email with lowercase
        user = User.query.filter_by(email=request.form["email"].lower()).first()
        # check if user exist
        if not user:
            # invalid email
            return jsonify({'success': False, 'message': 'Invalid email'}), 401
        else:
            password = request.form["password"]
            hash_pw = user.get_password()
            # Check if the password is correct
            if check_password_hash(hash_pw, password):
                # success login, store the user credentials in session
                session['id'] = user.id
                session['email'] = user.email
                session['first_name'] = user.first_name
                session['last_name'] = user.last_name
                return jsonify({'success': True, 'message': 'Login success'}), 200
            else:
                # invalid password
                return jsonify({'success': False, 'message': 'Invalid password'}), 401
    else:
        if 'id' in session:
            return redirect(url_for('chat.chat'))
        return render_template("login_view.html")

# get & post User
@login_blueprint.route('/me')
def get_me():
    if 'id' in session:
        user = User.query.filter_by(id=session['id']).first()
        return jsonify({'success': True, 'user': {'id': user.id, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}})
    else:
        return jsonify({'message': 'User not logged in'})

@login_blueprint.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('.login'))