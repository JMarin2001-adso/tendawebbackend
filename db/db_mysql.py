import pymysql
import os
from urllib.parse import urlparse

MYSQL_URL = os.getenv("MYSQL_URL")

if not MYSQL_URL:
    raise Exception("MYSQL_URL no está definida en las variables de entorno")

url = urlparse(MYSQL_URL)

MYSQL_USER = url.username
MYSQL_PASSWORD = url.password
MYSQL_HOST = url.hostname
MYSQL_PORT = url.port
MYSQL_DATABASE = url.path.lstrip("/")

class ConnectDB:
    def get_connection(self):
        try:
            connection = pymysql.connect(
                host=MYSQL_HOST,
                port=int(MYSQL_PORT),
                user=MYSQL_USER,
                password=MYSQL_PASSWORD,
                database=MYSQL_DATABASE,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Conexión exitosa a MySQL")
            return connection
        except Exception as e:
            print(f"Error en la conexión MySQL: {e}")
            return None

db_conn = ConnectDB()

def get_db_connection():
    return db_conn.get_connection()
