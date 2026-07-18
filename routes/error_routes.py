from flask import render_template


def registrar_manejadores_error(app):
    """
    Registra las páginas de error personalizadas de la aplicación.
    """

    @app.errorhandler(404)
    def pagina_no_encontrada(error):
        return render_template("errors/404.html"), 404

    @app.errorhandler(403)
    def acceso_denegado(error):
        return render_template("errors/403.html"), 403

    @app.errorhandler(500)
    def error_interno(error):
        return render_template("errors/500.html"), 500
    
#
# Por qué no se usa un Blueprint
# Porque estos manejadores no representan páginas normales con sus propias rutas. 
# Se registran directamente sobre la aplicación Flask.
#