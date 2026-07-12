from flask import Blueprint, send_file

from services.exportacion_service import crear_excel, crear_pdf
from services.cartera_service import obtener_cartera
from models.historico_model import obtener_historico_operaciones
from models.alarma_model import obtener_alarmas
from models.indice_model import obtener_indices
from models.ibex_model import obtener_acciones_ibex
from utils.auth import login_required


exportacion_bp = Blueprint("exportacion", __name__)


def enviar_excel(archivo, nombre):
    return send_file(
        archivo,
        as_attachment=True,
        download_name=nombre,
        mimetype=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )


def enviar_pdf(archivo, nombre):
    return send_file(
        archivo,
        as_attachment=True,
        download_name=nombre,
        mimetype="application/pdf"
    )


# --------------------------------------------------
# CARTERA
# --------------------------------------------------

def preparar_cartera():
    cartera = obtener_cartera()

    columnas = [
        "Ticker",
        "Nombre",
        "Nº acciones",
        "Precio medio",
        "Inversión",
        "Cotización actual",
        "Valor actual",
        "Rentabilidad",
        "Rentabilidad %"
    ]

    filas = []

    for posicion in cartera:
        filas.append([
            posicion["ticker"],
            posicion["nombre"],
            posicion["numero_acciones"],
            posicion["precio"],
            posicion["cargo"],
            posicion["cotizacion_actual"],
            posicion["valor_actual"],
            posicion["rentabilidad"],
            posicion["rentabilidad_porcentaje"]
        ])

    return columnas, filas


@exportacion_bp.route("/exportar/cartera/excel")
@login_required
def exportar_cartera_excel():
    columnas, filas = preparar_cartera()
    archivo = crear_excel("Mi cartera", columnas, filas)

    return enviar_excel(
        archivo,
        "cartera.xlsx"
    )


@exportacion_bp.route("/exportar/cartera/pdf")
@login_required
def exportar_cartera_pdf():
    columnas, filas = preparar_cartera()
    archivo = crear_pdf("Mi cartera", columnas, filas)

    return enviar_pdf(
        archivo,
        "cartera.pdf"
    )


# --------------------------------------------------
# HISTÓRICO
# --------------------------------------------------

def preparar_historico():
    operaciones = obtener_historico_operaciones()

    columnas = [
        "Tipo",
        "Ticker",
        "Nombre",
        "Nº acciones",
        "Precio",
        "Gastos",
        "Total",
        "Fecha",
        "Comentarios"
    ]

    filas = []

    for operacion in operaciones:
        importe = operacion["numero_acciones"] * operacion["precio"]

        if operacion["tipo"] == "COMPRA":
            total = importe + operacion["gastos"]
        else:
            total = importe - operacion["gastos"]

        filas.append([
            operacion["tipo"],
            operacion["ticker"],
            operacion["nombre"],
            operacion["numero_acciones"],
            operacion["precio"],
            operacion["gastos"],
            total,
            operacion["fecha"],
            operacion["comentarios"]
        ])

    return columnas, filas


@exportacion_bp.route("/exportar/historico/excel")
@login_required
def exportar_historico_excel():
    columnas, filas = preparar_historico()
    archivo = crear_excel("Histórico", columnas, filas)

    return enviar_excel(
        archivo,
        "historico_operaciones.xlsx"
    )


@exportacion_bp.route("/exportar/historico/pdf")
@login_required
def exportar_historico_pdf():
    columnas, filas = preparar_historico()
    archivo = crear_pdf(
        "Histórico de operaciones",
        columnas,
        filas
    )

    return enviar_pdf(
        archivo,
        "historico_operaciones.pdf"
    )


# --------------------------------------------------
# ALARMAS
# --------------------------------------------------

def preparar_alarmas():
    alarmas = obtener_alarmas()

    columnas = [
        "Ticker",
        "Nombre",
        "Cotización actual",
        "Tipo",
        "Precio objetivo",
        "Email",
        "SMS",
        "Estado"
    ]

    filas = []

    for alarma in alarmas:
        filas.append([
            alarma["ticker"],
            alarma["nombre"],
            alarma["cotizacion_actual"],
            alarma["tipo"],
            alarma["precio_objetivo"],
            "Sí" if alarma["notificar_email"] else "No",
            "Sí" if alarma["notificar_sms"] else "No",
            "Activa" if alarma["activa"] else "Inactiva"
        ])

    return columnas, filas


@exportacion_bp.route("/exportar/alarmas/excel")
@login_required
def exportar_alarmas_excel():
    columnas, filas = preparar_alarmas()
    archivo = crear_excel("Alarmas", columnas, filas)

    return enviar_excel(
        archivo,
        "alarmas.xlsx"
    )


@exportacion_bp.route("/exportar/alarmas/pdf")
@login_required
def exportar_alarmas_pdf():
    columnas, filas = preparar_alarmas()
    archivo = crear_pdf("Alarmas", columnas, filas)

    return enviar_pdf(
        archivo,
        "alarmas.pdf"
    )


# --------------------------------------------------
# ÍNDICES
# --------------------------------------------------

def preparar_indices():
    indices = obtener_indices()

    columnas = [
        "Índice",
        "Ticker Yahoo",
        "Cotización actual",
        "Variación",
        "Variación %"
    ]

    filas = []

    for indice in indices:
        filas.append([
            indice["nombre"],
            indice["ticker_yahoo"],
            indice["cotizacion_actual"],
            indice["variacion"],
            indice["variacion_porcentaje"]
        ])

    return columnas, filas


@exportacion_bp.route("/exportar/indices/excel")
@login_required
def exportar_indices_excel():
    columnas, filas = preparar_indices()
    archivo = crear_excel("Índices", columnas, filas)

    return enviar_excel(
        archivo,
        "indices.xlsx"
    )


@exportacion_bp.route("/exportar/indices/pdf")
@login_required
def exportar_indices_pdf():
    columnas, filas = preparar_indices()
    archivo = crear_pdf(
        "Información de índices",
        columnas,
        filas
    )

    return enviar_pdf(
        archivo,
        "indices.pdf"
    )


# --------------------------------------------------
# IBEX 35
# --------------------------------------------------

def preparar_ibex35():
    acciones = obtener_acciones_ibex()

    columnas = [
        "Ticker",
        "Nombre",
        "Ticker Yahoo",
        "Cotización",
        "Variación",
        "Variación %"
    ]

    filas = []

    for accion in acciones:
        filas.append([
            accion["ticker"],
            accion["nombre"],
            accion["ticker_yahoo"],
            accion["cotizacion_actual"],
            accion["variacion"],
            accion["variacion_porcentaje"]
        ])

    return columnas, filas


@exportacion_bp.route("/exportar/ibex35/excel")
@login_required
def exportar_ibex35_excel():
    columnas, filas = preparar_ibex35()
    archivo = crear_excel("IBEX 35", columnas, filas)

    return enviar_excel(
        archivo,
        "ibex35.xlsx"
    )


@exportacion_bp.route("/exportar/ibex35/pdf")
@login_required
def exportar_ibex35_pdf():
    columnas, filas = preparar_ibex35()
    archivo = crear_pdf(
        "Cotizaciones IBEX 35",
        columnas,
        filas
    )

    return enviar_pdf(
        archivo,
        "ibex35.pdf"
    )