from database.conexion import obtener_conexion

def obtener_operaciones():
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
                    o.fecha
                FROM operaciones o
                INNER JOIN valores v
                    ON o.valor_id = v.id
                ORDER BY o.fecha
            """
            cursor.execute(sql)
            operaciones = cursor.fetchall()
            return operaciones

    finally:
        conexion.close()