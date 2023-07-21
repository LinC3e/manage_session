import mysql.connector
from mysql.connector import errors
from dotenv import load_dotenv
import os

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

def conectar():
    """Conectar con la base de datos y devolver un obj conexion."""
    try:
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASS'),
            database=os.getenv('MYSQL_DB')
        )
    except errors.DatabaseError as err:
        print("Error al conectar.", err)
    else:
        print("Conexión exitosa a la base de datos.")
        return conn
