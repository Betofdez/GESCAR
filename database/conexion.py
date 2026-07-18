import pymysql

from config import Config


def obtener_conexion():
    """
    Crea y devuelve una conexión con la base de datos MySQL.
    """
    return pymysql.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )