"""
Configuración de la aplicación.

Separar la configuración del código de la aplicación es una buena práctica:
permite tener valores distintos para desarrollo, pruebas y producción sin
tocar la lógica del programa.
"""

import os

# Ruta absoluta a la carpeta raíz del proyecto (donde está run.py).
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuración base (desarrollo)."""

    # Clave usada por Flask para firmar cookies/sesiones.
    #En un proyecto real se lee de una variable de entorno:
    SECRET_KEY = os.environ.get("SECRET_KEY", "mi-clave-secreta-super-segura")

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(
        BASE_DIR, "instance", "tienda.db"
    )
    # Desactiva un sistema de eventos de SQLAlchemy que no usamos.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO =True
