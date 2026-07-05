from flask import Blueprint, render_template
from utils.auth import login_required

inicio_bp = Blueprint("inicio", __name__)

@inicio_bp.route("/")
@login_required
def inicio():
    return render_template("inicio.html")