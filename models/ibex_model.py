from database.conexion import obtener_conexion


def obtener_acciones_ibex():
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, ticker, nombre, ticker_yahoo,
                       cotizacion_actual, variacion, variacion_porcentaje
                FROM acciones_ibex
                ORDER BY ticker
            """)
            return cursor.fetchall()
    finally:
        conexion.close()


def actualizar_accion_ibex(accion_id, cotizacion_actual, variacion, variacion_porcentaje):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                UPDATE acciones_ibex
                SET cotizacion_actual = %s,
                    variacion = %s,
                    variacion_porcentaje = %s
                WHERE id = %s
            """, (cotizacion_actual, variacion, variacion_porcentaje, accion_id))
            conexion.commit()
    finally:
        conexion.close()