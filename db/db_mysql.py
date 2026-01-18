import os
import pymysql
from urllib.parse import urlparse

MYSQL_URL = os.getenv("MYSQL_URL")

if not MYSQL_URL:
    print("⚠️ MYSQL_URL no definida. Esperando entorno...")
    MYSQL_URL = None
else:
    url = urlparse(MYSQL_URL)

    MYSQL_USER = url.username
    MYSQL_PASSWORD = url.password
    MYSQL_HOST = url.hostname
    MYSQL_PORT = url.port
    MYSQL_DATABASE = url.path.lstrip("/")


class ConnectDB:
    def get_connection(self):
        if not MYSQL_URL:
            raise Exception("MYSQL_URL no configurada")

        return pymysql.connect(
            host=MYSQL_HOST,
            port=int(MYSQL_PORT),
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            cursorclass=pymysql.cursors.DictCursor
        )


db_conn = ConnectDB()

def get_db_connection():
    return db_conn.get_connection()
