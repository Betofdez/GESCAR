from flask import Blueprint, render_template
from models.historico_model import obtener_historico_operaciones
from utils.auth import login_required

historico_bp = Blueprint("historico", __name__)

@historico_bp.route("/historico")
@login_required
def historico():
    operaciones = obtener_historico_operaciones()
    return render_template("historico.html", operaciones=operaciones)

