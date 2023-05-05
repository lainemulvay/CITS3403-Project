from flask import Flask,render_template,flash, redirect,url_for,session,logging,request, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
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

#login
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
                # success login
                return jsonify({'success': True, 'message': 'Login success'}), 200
            else:
                # invalid password
                return jsonify({'success': False, 'message': 'Invalid password'}), 401
    return render_template("login_view.html")

# register
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

@app.route("/history/")
def history():
    return render_template("hist_view.html", display = True)

@app.route("/chat/")
def chat():
    return render_template("chat_view.html", display = True)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)