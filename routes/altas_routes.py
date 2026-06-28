from flask import Blueprint, render_template, request, redirect
from models.valor_model import obtener_valores
from models.operacion_model import insertar_compra

altas_bp = Blueprint("altas", __name__)

@altas_bp.route("/altas", methods=["GET", "POST"])
def altas():

    if request.method == "POST":
        valor_id = request.form["valor_id"]
        numero_acciones = request.form["numero_acciones"]
        precio = request.form["precio"]
        gastos = request.form["gastos"]
        fecha = request.form["fecha"]
        comentarios = request.form["comentarios"]

        insertar_compra(
            usuario_id=1,
            valor_id=valor_id,
            numero_acciones=numero_acciones,
            precio=precio,
            gastos=gastos,
            fecha=fecha,
            comentarios=comentarios
        )

        return redirect("/cartera")

    valores = obtener_valores()
    return render_template("altas.html", valores=valores)