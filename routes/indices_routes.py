from flask import Blueprint, render_template

indices_bp = Blueprint("indices", __name__)

@indices_bp.route("/indices")
def indices():
    return render_template("indices.html")