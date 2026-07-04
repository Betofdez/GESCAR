from models.cartera_model import obtener_operaciones
from domain.cartera import Cartera


def obtener_cartera():
    operaciones = obtener_operaciones()
    cartera = Cartera(operaciones)

    resultado = []

    for posicion in cartera.posiciones:
        resultado.append({
            "ticker": posicion.valor.ticker,
            "nombre": posicion.valor.nombre,
            "numero_acciones": posicion.numero_acciones,
            "precio": posicion.precio_medio(),
            "total": posicion.inversion_total,
            "gastos": 0,
            "cargo": posicion.inversion_total,
            "cotizacion_actual": posicion.valor.cotizacion_actual,
            "valor_actual": posicion.valor_actual(),
            "rentabilidad": posicion.rentabilidad(),
            "rentabilidad_porcentaje": posicion.rentabilidad_porcentaje(),
            "fecha": ""
        })

    return resultado


def obtener_resumen_cartera():
    operaciones = obtener_operaciones()
    cartera = Cartera(operaciones)

    return {
        "valor_total": cartera.valor_total(),
        "inversion_total": cartera.inversion_total(),
        "rentabilidad_total": cartera.rentabilidad_total(),
        "rentabilidad_porcentaje_total": cartera.rentabilidad_porcentaje_total(),
        "numero_valores": cartera.numero_valores(),
        "dividendos": 0
    }

def obtener_posicion(ticker):
    operaciones = obtener_operaciones()
    cartera = Cartera(operaciones)

    return cartera.obtener_posicion_por_ticker(ticker)