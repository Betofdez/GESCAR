import yfinance as yf
from models.indice_model import obtener_indices, actualizar_indice


def actualizar_indices():
    indices = obtener_indices()
    actualizados = 0

    for indice in indices:
        ticker = indice["ticker_yahoo"]

        datos = yf.Ticker(ticker).history(period="5d")

        if datos.empty or len(datos) < 2:
            continue

        cierre_anterior = float(datos["Close"].iloc[-2])
        cierre_actual = float(datos["Close"].iloc[-1])

        variacion = cierre_actual - cierre_anterior

        if cierre_anterior != 0:
            variacion_porcentaje = (variacion / cierre_anterior) * 100
        else:
            variacion_porcentaje = 0

        actualizar_indice(
            indice_id=indice["id"],
            cotizacion_actual=cierre_actual,
            variacion=variacion,
            variacion_porcentaje=variacion_porcentaje
        )

        actualizados += 1

    return actualizados