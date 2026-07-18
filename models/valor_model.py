from database.conexion import obtener_conexion
from domain.valor import Valor


def obtener_valores():
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    id,
                    ticker,
                    nombre,
                    cotizacion_actual
                FROM valores
                ORDER BY ticker
            """

            cursor.execute(sql)
            filas = cursor.fetchall()

            valores = []

            for fila in filas:
                valor = Valor(
                    id=fila["id"],
                    ticker=fila["ticker"],
                    nombre=fila["nombre"],
                    cotizacion_actual=fila["cotizacion_actual"]
                )

                valores.append(valor)

            return valores

    finally:
        conexion.close()

def obtener_valor_por_ticker(ticker):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, ticker, nombre, cotizacion_actual
                FROM valores
                WHERE ticker = %s
            """

            cursor.execute(sql, (ticker,))
            fila = cursor.fetchone()

            if fila is None:
                return None

            return Valor(
                id=fila["id"],
                ticker=fila["ticker"],
                nombre=fila["nombre"],
                cotizacion_actual=fila["cotizacion_actual"]
            )

    finally:
        conexion.close()

def obtener_valor_por_ticker_y_mercado(ticker, mercado):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    id,
                    ticker,
                    nombre,
                    cotizacion_actual
                FROM valores
                WHERE ticker = %s
                  AND mercado = %s
            """

            cursor.execute(sql, (ticker, mercado))
            fila = cursor.fetchone()

            if fila is None:
                return None

            return Valor(
                id=fila["id"],
                ticker=fila["ticker"],
                nombre=fila["nombre"],
                cotizacion_actual=fila["cotizacion_actual"]
            )

    finally:
        conexion.close()


def insertar_valor_ibex(accion):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO valores (
                    ticker,
                    nombre,
                    mercado,
                    pais,
                    divisa,
                    cotizacion_actual,
                    ticker_yahoo,
                    activo
                )
                VALUES (%s, %s, 'BME', 'España', 'EUR', %s, %s, TRUE)
            """

            cursor.execute(sql, (
                accion["ticker"],
                accion["nombre"],
                accion["cotizacion_actual"],
                accion["ticker_yahoo"]
            ))

            conexion.commit()

            # Cuando MySQL crea el nuevo valor, genera automáticamente su id. 
            # Esta instrucción devuelve ese identificador para usarlo en la nueva operación.
            return cursor.lastrowid

    finally:
        conexion.close()

def obtener_o_crear_valor_ibex(accion):
    valor = obtener_valor_por_ticker_y_mercado(
        accion["ticker"],
        "BME"
    )

    if valor is not None:
        return valor.id

    return insertar_valor_ibex(accion)