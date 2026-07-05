from flask import Blueprint, render_template, redirect, flash
from models.indice_model import obtener_indices
from services.indice_service import actualizar_indices
from utils.auth import login_required

indices_bp = Blueprint("indices", __name__)

@indices_bp.route("/indices")
@login_required
def indices():
    datos_indices = obtener_indices()
    return render_template("indices.html", indices=datos_indices)


@indices_bp.route("/indices/actualizar")
@login_required
def actualizar():
    actualizados = actualizar_indices()
    flash(f"Se han actualizado {actualizados} índices correctamente.", "success")
    return redirect("/indices")