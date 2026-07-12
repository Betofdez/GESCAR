from flask import Flask

from routes.inicio_routes import inicio_bp
from routes.cartera_routes import cartera_bp
from routes.historico_routes import historico_bp
from routes.indices_routes import indices_bp
from routes.alarmas_routes import alarmas_bp
from routes.altas_routes import altas_bp
from routes.venta_routes import venta_bp
from routes.cotizacion_routes import cotizacion_bp
from routes.login_routes import login_bp
from routes.ibex_routes import ibex_bp
from routes.exportacion_routes import exportacion_bp

from filters.formatos import formato_es
from filters.formatos import fecha_es

app = Flask(__name__)
app.secret_key = "gescar_clave_desarrollo"

app.register_blueprint(inicio_bp)
app.register_blueprint(cartera_bp)
app.register_blueprint(historico_bp)
app.register_blueprint(indices_bp)
app.register_blueprint(alarmas_bp)
app.register_blueprint(altas_bp)
app.register_blueprint(venta_bp)
app.register_blueprint(cotizacion_bp)
app.register_blueprint(login_bp)
app.register_blueprint(ibex_bp)
app.register_blueprint(exportacion_bp)


# Formatos numéricos en español
app.jinja_env.filters["formato_es"] = formato_es
app.jinja_env.filters["fecha_es"] = fecha_es

if __name__ == "__main__":
    app.run(debug=True)