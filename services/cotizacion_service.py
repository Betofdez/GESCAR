import yfinance as yf
from database.conexion import obtener_conexion


def actualizar_cotizaciones():
    conexion = obtener_conexion()
    actualizados = 0

    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, ticker, ticker_yahoo
                FROM valores
                WHERE activo = TRUE
            """)

            valores = cursor.fetchall()

            for valor in valores:
                if not valor["ticker_yahoo"]:
                    continue

                ticker_yahoo = valor["ticker_yahoo"]
                info = yf.Ticker(ticker_yahoo)
                datos = info.history(period="1d")

                if datos.empty:
                    continue

                precio = float(datos["Close"].iloc[-1])

                cursor.execute("""
                    UPDATE valores
                    SET cotizacion_actual = %s
                    WHERE id = %s
                """, (precio, valor["id"]))

                actualizados += 1

            conexion.commit()

    finally:
        conexion.close()

    return actualizados