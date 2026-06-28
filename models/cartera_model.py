from database.conexion import obtener_conexion
from domain.valor import Valor
from domain.operacion import Operacion


def obtener_operaciones():
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:

            sql = """
                SELECT
                    o.id,
                    v.id AS valor_id,
                    v.ticker,
                    v.nombre,
                    v.cotizacion_actual,
                    o.numero_acciones,
                    o.precio,
                    o.tipo,
                    o.gastos,
                    o.fecha
                FROM operaciones o
                INNER JOIN valores v
                    ON o.valor_id = v.id
                ORDER BY o.fecha
            """

            cursor.execute(sql)
            filas = cursor.fetchall()

            operaciones = []

            for fila in filas:
                valor = Valor(
                    id=fila["valor_id"],
                    ticker=fila["ticker"],
                    nombre=fila["nombre"],
                    cotizacion_actual=fila["cotizacion_actual"]
                )

                operacion = Operacion(
                    id=fila["id"],
                    valor=valor,
                    tipo=fila["tipo"],
                    numero_acciones=fila["numero_acciones"],
                    precio=fila["precio"],
                    gastos=fila["gastos"],
                    fecha=fila["fecha"]
                )

                operaciones.append(operacion)

            return operaciones

    finally:
        conexion.close()