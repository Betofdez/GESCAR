from flask import Blueprint, render_template
from models.historico_model import obtener_ventas

historico_bp = Blueprint("historico", __name__)

@historico_bp.route("/historico")
def historico():
    ventas = obtener_ventas()
    return render_template("historico.html", ventas=ventas)

