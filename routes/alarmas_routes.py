from flask import Blueprint, render_template, request, redirect, session, flash
from models.alarma_model import obtener_alarmas, insertar_alarma
from models.valor_model import obtener_valores
from utils.auth import login_required

alarmas_bp = Blueprint("alarmas", __name__)


@alarmas_bp.route("/alarmas", methods=["GET", "POST"])
@login_required
def alarmas():

    if request.method == "POST":
        valor_id = request.form["valor_id"]
        tipo = request.form["tipo"]
        precio_objetivo = request.form["precio_objetivo"]

        notificar_email = "notificar_email" in request.form
        notificar_sms = "notificar_sms" in request.form

        insertar_alarma(
            usuario_id=session["usuario_id"],
            valor_id=valor_id,
            tipo=tipo,
            precio_objetivo=precio_objetivo,
            notificar_email=notificar_email,
            notificar_sms=notificar_sms
        )

        flash("Alarma creada correctamente.", "success")
        return redirect("/alarmas")

    datos_alarmas = obtener_alarmas()
    valores = obtener_valores()

    return render_template(
        "alarmas.html",
        alarmas=datos_alarmas,
        valores=valores
    )