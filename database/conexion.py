import pymysql

def obtener_conexion():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="gescar_db",
        cursorclass=pymysql.cursors.DictCursor # devuelve los datos como diccionario
    )