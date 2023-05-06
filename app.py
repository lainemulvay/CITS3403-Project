from flask import Flask,render_template,flash, redirect, url_for, session,logging, request, jsonify, make_response
# from flask_login import LoginManager, login_required, current_user, login_user
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey' # secret key for session security
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    first_name = db.Column("First Name", db.String(100), nullable=False)
    last_name = db.Column("Last Name", db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User %r>' % self.email

    def get_password(self):
        return self.password
    
@app.route("/")
@app.route("/index/")
def index():
    return render_template("intro_view.html")

# get & post User
@app.route('/me')
def get_me():
    if 'id' in session:
        user = User.query.filter_by(id=session['id']).first()
        return jsonify({'success': True, 'user': {'id': user.id, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name}})
    else:
        return jsonify({'message': 'User not logged in'})

# login function
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form["email"]).first()
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
    return render_template("login_view.html")

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

# register function
@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User.query.filter_by(email=request.form['email']).first()
        print(user)
        # Check if the user exists
        if user:
            # return render_template("reg_view.html", msg = "Email already exists")
            return jsonify({'success': False, 'message': 'Email already exists'}), 401
    
        email = request.form['email']
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        password = request.form['newPW']
        hashed_pw = generate_password_hash(password, method='sha256')
        register = User(email= email, first_name = first_name, last_name = last_name, password = hashed_pw)
        print(register)
        db.session.add(register)
        db.session.commit()
        
        return jsonify({'success': True, 'message': 'Account successfully created'}), 200
    return render_template("reg_view.html")

# history page
@app.route("/history/")
def history():
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login'))
    return render_template("hist_view.html", display = True)

# chat page
@app.route("/chat/")
def chat():
    if 'email' not in session:
        flash('Please log in to view this page', 'danger')
        return redirect(url_for('login'))
    return render_template('chat_view.html', display=True)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    response.headers['Vary'] = 'User-Agent'
    return response

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)