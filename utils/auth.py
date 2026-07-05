from functools import wraps
from flask import session, redirect, flash

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if "usuario_id" not in session:
            flash("Debes iniciar sesión para acceder.", "warning")
            return redirect("/login")

        return func(*args, **kwargs)

    return wrapper