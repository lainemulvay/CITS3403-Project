from app.controller import get_user, update_user, change_password
from flask import render_template,flash, redirect, url_for, session, request, jsonify
# from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import check_password_hash
from app.profile import profile_blueprint

@profile_blueprint.route("/profile/", methods=["GET", "POST"])
def profile():
    # check if user is logged in
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login.login'))
    
    # get user details
    firstname = get_user().first_name
    lastname = get_user().last_name
    email = get_user().email

    if request.method == "POST":
        action = request.form['action']
        id = get_user().id

        # update user details
        if action == 'update_account':
            email = request.form['email'].lower()
            first_name = request.form['firstname']
            last_name = request.form['lastname']
            update = update_user(id, email, first_name, last_name)
            print(update)
            # return json statement
            return jsonify({'success': True, 'message': 'Account updated'}), 200
        
        # update password
        elif action == 'update_password':
            user = get_user()
            oldpw = request.form['oldpw']
            hash_pw = user.get_password()
            if check_password_hash(hash_pw, oldpw):
                newpw = request.form['newpw']
                updatepw = change_password(id, newpw)
                print(updatepw)
                return jsonify({'success': True, 'message': 'Password updated'}), 200
            else:
                # check_password_hash not match
                return jsonify({'success': False, 'message': 'Existing password is not correct, please try again'}), 401

    # return with user details
    return render_template("profile_view.html", display = True, username=firstname, firstname=firstname, lastname=lastname, email=email)