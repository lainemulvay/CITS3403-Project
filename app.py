from flask import Flask, escape, render_template

app = Flask(__name__)

@app.route("/intro")
def index():
    return render_template("intro_view.html")

if __name__ == "__main__":
    app.run(debug=True)