from flask import Blueprint, render_template, request, redirect
from models.valor_model import obtener_valor_por_ticker
from models.operacion_model import insertar_venta

venta_bp = Blueprint("venta", __name__)

@venta_bp.route("/venta/<ticker>", methods=["GET", "POST"])
def venta(ticker):
    valor = obtener_valor_por_ticker(ticker)

    if valor is None:
        return redirect("/cartera")

    if request.method == "POST":
        numero_acciones = request.form["numero_acciones"]
        precio = request.form["precio"]
        gastos = request.form["gastos"]
        fecha = request.form["fecha"]
        comentarios = request.form["comentarios"]

        insertar_venta(
            usuario_id=1,
            valor_id=valor.id,
            numero_acciones=numero_acciones,
            precio=precio,
            gastos=gastos,
            fecha=fecha,
            comentarios=comentarios
        )

        return redirect("/cartera")

    return render_template("venta.html", valor=valor)