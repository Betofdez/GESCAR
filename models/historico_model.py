from database.conexion import obtener_conexion


def obtener_ventas():
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    o.id,
                    v.ticker,
                    v.nombre,
                    o.numero_acciones,
                    o.precio,
                    o.gastos,
                    o.fecha,
                    o.comentarios
                FROM operaciones o
                INNER JOIN valores v
                    ON o.valor_id = v.id
                WHERE o.tipo = 'VENTA'
                ORDER BY o.fecha DESC
            """

            cursor.execute(sql)
            return cursor.fetchall()

    finally:
        conexion.close()