from flask import Flask,render_template,flash, redirect,url_for,session,logging,request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "project_1"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

class users(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    First_Name = db.Column("First Name", db.String(100), nullable=False)
    Last_Name = db.Column("Last Name", db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


@app.route("/")
def index():
    return render_template("intro_view.html")

#login
@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        login = user.query.filter_by(username=email, password=password).first()
        if login is not None:
            return redirect(url_for('chat'))
    return render_template("login_view.html")

@app.route("/register/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        email = request.form['email']
        First_name = request.form['firstname']
        Last_name = request.form['lastname']
        password = request.form['password']
        register = user(username = email, First_name = First_name, Last_name = Last_name, password = password)
        db.session.add(register)
        db.session.commit()
        
        return redirect(url_for('chat'))
    return render_template("reg_view.html")


@app.route("/history/")
def history():
    return render_template("hist_view.html", display = True)

@app.route("/chat/")
def chat():
    return render_template("chat_view.html", display = True)

if __name__ == "__main__":
    app.run(debug=True)


'''
@app.route("/user", methods = ["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]
        
        if request.method == "POST":
            email = request.form["email"]
        return render_template("reg_view.html")

@app.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again
        return redirect(url_for('auth.signup'))

    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return render_template("login_view.html")

@auth.route('/login', methods=['POST'])
def login_post():
    # login code goes here
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    # check if the user actually exists
    # take the user-supplied password, hash it, and compare it to the hashed password in the database
    if not user or not check_password_hash(user.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login')) # if the user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    return redirect(url_for('main.profile'))

'''