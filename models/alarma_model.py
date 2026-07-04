from database.conexion import obtener_conexion


def obtener_alarmas():
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT
                    a.id,
                    v.ticker,
                    v.nombre,
                    v.cotizacion_actual,
                    a.tipo,
                    a.precio_objetivo,
                    a.activa,
                    a.notificar_email,
                    a.notificar_sms
                FROM alarmas a
                INNER JOIN valores v
                    ON a.valor_id = v.id
                ORDER BY v.ticker
            """

            cursor.execute(sql)
            return cursor.fetchall()

    finally:
        conexion.close()