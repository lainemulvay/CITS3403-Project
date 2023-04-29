from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route("/intro")
def index():
    return render_template("intro_view.html")

@app.route("/login")
def login():
    return render_template("login_view.html")

@app.route("/register")
def register():
    return render_template("reg_view.html")

@app.route("/history")
def history():
    return render_template("hist_view.html")

@app.route("/chat")
def chat():
    return render_template("chat_view.html")

if __name__ == "__main__":
    app.run(debug=True)