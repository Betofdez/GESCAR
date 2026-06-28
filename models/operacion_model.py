from database.conexion import obtener_conexion


def insertar_compra(usuario_id, valor_id, numero_acciones, precio, gastos, fecha, comentarios):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO operaciones
                    (usuario_id, valor_id, tipo, numero_acciones, precio, gastos, fecha, comentarios)
                VALUES
                    (%s, %s, 'COMPRA', %s, %s, %s, %s, %s)
            """

            cursor.execute(sql, (
                usuario_id,
                valor_id,
                numero_acciones,
                precio,
                gastos,
                fecha,
                comentarios
            ))

            conexion.commit()

    finally:
        conexion.close()

def insertar_venta(usuario_id, valor_id, numero_acciones, precio, gastos, fecha, comentarios):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                INSERT INTO operaciones
                    (usuario_id, valor_id, tipo, numero_acciones, precio, gastos, fecha, comentarios)
                VALUES
                    (%s, %s, 'VENTA', %s, %s, %s, %s, %s)
            """

            cursor.execute(sql, (
                usuario_id,
                valor_id,
                numero_acciones,
                precio,
                gastos,
                fecha,
                comentarios
            ))

            conexion.commit()

    finally:
        conexion.close()