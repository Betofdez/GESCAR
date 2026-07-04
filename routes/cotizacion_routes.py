from flask import Blueprint, redirect, flash
from services.cotizacion_service import actualizar_cotizaciones

cotizacion_bp = Blueprint("cotizacion", __name__)

@cotizacion_bp.route("/cotizaciones/actualizar")
def actualizar():
    actualizados = actualizar_cotizaciones()

    flash(f"Se han actualizado {actualizados} cotizaciones correctamente.", "success")

    return redirect("/cartera")