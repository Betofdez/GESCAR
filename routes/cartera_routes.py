from flask import Blueprint, render_template
from services.cartera_service import obtener_cartera, obtener_resumen_cartera
from utils.auth import login_required

cartera_bp = Blueprint("cartera", __name__)

@cartera_bp.route("/cartera")
@login_required
def cartera():
    datos_cartera = obtener_cartera()
    resumen = obtener_resumen_cartera()

    return render_template(
        "cartera.html",
        cartera=datos_cartera,
        resumen=resumen
    )