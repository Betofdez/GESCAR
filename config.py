import os

from dotenv import load_dotenv


load_dotenv()


class Config:
    """
    Configuración general de la aplicación GESCAR.

    Los valores se obtienen del archivo .env y pueden modificarse
    sin alterar el código fuente.
    """

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "clave-desarrollo-por-defecto"
    )

    DB_HOST = os.getenv(
        "DB_HOST",
        "localhost"
    )

    DB_PORT = int(
        os.getenv("DB_PORT", "3306")
    )

    DB_USER = os.getenv(
        "DB_USER",
        "root"
    )

    DB_PASSWORD = os.getenv(
        "DB_PASSWORD",
        ""
    )

    DB_NAME = os.getenv(
        "DB_NAME",
        "gescar_db"
    )

    DEBUG = os.getenv(
        "FLASK_DEBUG",
        "False"
    ).lower() in ("true", "1", "yes")