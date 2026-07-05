from flask import Blueprint, redirect, flash
from services.cotizacion_service import actualizar_cotizaciones
from utils.auth import login_required

cotizacion_bp = Blueprint("cotizacion", __name__)

@cotizacion_bp.route("/cotizaciones/actualizar")
@login_required
def actualizar():
    actualizados = actualizar_cotizaciones()

    flash(f"Se han actualizado {actualizados} cotizaciones correctamente.", "success")

    return redirect("/cartera")