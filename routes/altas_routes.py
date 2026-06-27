from flask import Blueprint, render_template

altas_bp = Blueprint("altas", __name__)

@altas_bp.route("/altas")
def altas():
    return render_template("altas.html")