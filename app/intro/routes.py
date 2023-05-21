from flask import render_template
from app.intro import intro_blueprint

# intro page
@intro_blueprint.route("/")
def index():
    return render_template("intro_view.html")