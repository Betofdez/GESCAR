from flask import Blueprint, render_template

alarmas_bp = Blueprint("alarmas", __name__)

@alarmas_bp.route("/alarmas")
def alarmas():
    return render_template("alarmas.html")