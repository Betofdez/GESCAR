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