from flask import Blueprint, render_template
from utils.auth import login_required

indices_bp = Blueprint("indices", __name__)

@indices_bp.route("/indices")
@login_required
def indices():
    return render_template("indices.html")