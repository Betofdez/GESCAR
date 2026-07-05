import yfinance as yf
from models.ibex_model import obtener_acciones_ibex, actualizar_accion_ibex


def actualizar_acciones_ibex():
    acciones = obtener_acciones_ibex()
    actualizadas = 0

    for accion in acciones:
        datos = yf.Ticker(accion["ticker_yahoo"]).history(period="5d")

        if datos.empty or len(datos) < 2:
            continue

        cierre_anterior = float(datos["Close"].iloc[-2])
        cierre_actual = float(datos["Close"].iloc[-1])
        variacion = cierre_actual - cierre_anterior
        variacion_porcentaje = (variacion / cierre_anterior) * 100 if cierre_anterior else 0

        actualizar_accion_ibex(
            accion["id"],
            cierre_actual,
            variacion,
            variacion_porcentaje
        )

        actualizadas += 1

    return actualizadas