from flask import Blueprint, render_template

historico_bp = Blueprint("historico", __name__)

@historico_bp.route("/historico")
def historico():
    return render_template("historico.html")