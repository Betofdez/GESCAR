from flask import Blueprint, render_template, request, redirect
from models.valor_model import obtener_valor_por_ticker
from models.operacion_model import insertar_venta
from services.cartera_service import obtener_posicion

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

        posicion = obtener_posicion(ticker)

        if posicion is None or float(numero_acciones) > float(posicion.numero_acciones):
            return render_template(
                "venta.html",
                valor=valor,
                posicion=posicion,
                error="No puedes vender más acciones de las que tienes."
            )
        
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

    posicion = obtener_posicion(ticker)
    return render_template("venta.html", valor=valor, posicion=posicion)