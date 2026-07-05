from database.conexion import obtener_conexion

def obtener_usuario_por_username(username):
    conexion = obtener_conexion()

    try:
        with conexion.cursor() as cursor:
            sql = """
                SELECT id, nombre, apellidos, usuario, email, password_hash
                FROM usuarios
                WHERE usuario = %s
            """

            cursor.execute(sql, (username,))
            return cursor.fetchone()

    finally:
        conexion.close()