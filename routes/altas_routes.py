from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    flash
)

from models.ibex_model import (
    obtener_acciones_ibex,
    obtener_accion_ibex_por_id
)

from models.valor_model import obtener_o_crear_valor_ibex
from models.operacion_model import insertar_compra
from utils.auth import login_required


altas_bp = Blueprint("altas", __name__)


@altas_bp.route("/altas", methods=["GET", "POST"])
@login_required
def altas():

    if request.method == "POST":
        accion_ibex_id = request.form["accion_ibex_id"]

        accion_ibex = obtener_accion_ibex_por_id(
            accion_ibex_id
        )

        if accion_ibex is None:
            flash(
                "La acción seleccionada no existe.",
                "danger"
            )
            return redirect("/altas")

        valor_id = obtener_o_crear_valor_ibex(
            accion_ibex
        )

        numero_acciones = request.form["numero_acciones"]
        precio = request.form["precio"]
        gastos = request.form.get("gastos", 0)
        fecha = request.form["fecha"]
        comentarios = request.form.get("comentarios", "")

        insertar_compra(
            usuario_id=session["usuario_id"],
            valor_id=valor_id,
            numero_acciones=numero_acciones,
            precio=precio,
            gastos=gastos,
            fecha=fecha,
            comentarios=comentarios
        )

        flash(
            "Compra registrada correctamente.",
            "success"
        )

        return redirect("/cartera")

    acciones_ibex = obtener_acciones_ibex()

    return render_template(
        "altas.html",
        acciones_ibex=acciones_ibex
    )