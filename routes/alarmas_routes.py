from flask import Blueprint, render_template
from models.alarma_model import obtener_alarmas

alarmas_bp = Blueprint("alarmas", __name__)

@alarmas_bp.route("/alarmas")
def alarmas():
    datos_alarmas = obtener_alarmas()
    return render_template("alarmas.html", alarmas=datos_alarmas)