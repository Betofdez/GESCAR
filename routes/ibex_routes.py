from flask import Blueprint, render_template, redirect, flash
from models.ibex_model import obtener_acciones_ibex
from services.ibex_service import actualizar_acciones_ibex
from utils.auth import login_required

ibex_bp = Blueprint("ibex", __name__)


@ibex_bp.route("/ibex35")
@login_required
def ibex35():
    acciones = obtener_acciones_ibex()
    return render_template("ibex35.html", acciones=acciones)


@ibex_bp.route("/ibex35/actualizar")
@login_required
def actualizar_ibex35():
    actualizadas = actualizar_acciones_ibex()
    flash(f"Se han actualizado {actualizadas} acciones del IBEX 35.", "success")
    return redirect("/ibex35")