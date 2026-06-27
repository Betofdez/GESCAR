from flask import Blueprint, render_template

cartera_bp = Blueprint("cartera", __name__)

@cartera_bp.route("/cartera")
def cartera():
    return render_template("cartera.html")