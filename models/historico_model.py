from database.conexion import obtener_conexion


def obtener_historico_operaciones():
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    o.id,
                    o.tipo,
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
                ORDER BY o.fecha DESC, o.id DESC
            """

            cursor.execute(sql)
            return cursor.fetchall()

    finally:
        conexion.close()