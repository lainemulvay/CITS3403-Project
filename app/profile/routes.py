from app import app, db
from app.models import User
from app.controller import get_user, update_user
from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.profile import profile_blueprint

@profile_blueprint.route("/profile/", methods=["GET", "POST"])
def profile():
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    firstname = get_user().first_name
    lastname = get_user().last_name
    email = get_user().email

    if request.method == "POST":
        id = get_user().id
        email = request.form['email'].lower()
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        update = update_user(id, email, first_name, last_name)
        print(update)

        return jsonify({'success': True, 'message': 'Account updated'}), 200

    # return user details
    return render_template("profile_view.html", display = True, username=firstname, firstname=firstname, lastname=lastname, email=email)