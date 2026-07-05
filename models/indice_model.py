from database.conexion import obtener_conexion


def obtener_indices():
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, nombre, ticker_yahoo, cotizacion_actual,
                       variacion, variacion_porcentaje
                FROM indices
                ORDER BY nombre
            """)
            return cursor.fetchall()

    finally:
        conexion.close()

def actualizar_indice(indice_id, cotizacion_actual, variacion, variacion_porcentaje):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                UPDATE indices
                SET cotizacion_actual = %s,
                    variacion = %s,
                    variacion_porcentaje = %s
                WHERE id = %s
            """

            cursor.execute(sql, (
                cotizacion_actual,
                variacion,
                variacion_porcentaje,
                indice_id
            ))

            conexion.commit()

    finally:
        conexion.close()