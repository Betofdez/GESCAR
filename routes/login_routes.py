from flask import Blueprint, render_template, request, redirect, session, flash
from werkzeug.security import check_password_hash
from models.usuario_model import obtener_usuario_por_username

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["usuario"]
        password = request.form["password"]

        usuario = obtener_usuario_por_username(username)

        if usuario and check_password_hash(usuario["password_hash"], password):
            session["usuario_id"] = usuario["id"]
            session["usuario"] = usuario["usuario"]
            session["nombre"] =  f"{usuario['nombre']} {usuario['apellidos']}"

            flash("Has iniciado sesión correctamente.", "success")
            return redirect("/")

        flash("Usuario o contraseña incorrectos.", "danger")

    return render_template("login.html")


@login_bp.route("/logout")
def logout():
    session.clear()
    flash("Has cerrado sesión correctamente.", "info")
    return redirect("/login")