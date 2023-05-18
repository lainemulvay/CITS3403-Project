from flask import render_template
# from flask_login import LoginManager, login_required, current_user, login_user
from app.intro import intro_blueprint

# intro page
@intro_blueprint.route("/")
def index():
    return render_template("intro_view.html")