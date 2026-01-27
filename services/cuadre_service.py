import pymysql
from db.db_mysql import get_db_connection
from models.cuadre_model import CuadreCajaIn

class CuadreCajaService:

    def __init__(self):
        self.con = get_db_connection()

    # 🔹 Ventas del día (para el frontend)
    def obtener_ventas_diarias(self, fecha: str, id_usuario: int):
        try:
            self.con.ping(reconnect=True)
            with self.con.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute("""
                    SELECT
                        f.id_factura,
                        f.numero_factura,
                        f.total,
                        f.fecha
                    FROM factura f
                    WHERE DATE(f.fecha) = %s
                      AND f.id_usuario = %s
                      AND f.estado = 'emitida'
                      AND f.origen = 'fisica'
                """, (fecha, id_usuario))

                ventas = cursor.fetchall()

                total_sistema = sum(v["total"] for v in ventas)

                return {
                    "success": True,
                    "ventas": ventas,
                    "total_sistema": total_sistema
                }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

        finally:
            self.close_connection()

    # 🔹 Guardar cuadre de caja
    def guardar_cuadre_caja(self, data:CuadreCajaIn):
        try:
            diferencia = data.dinero_caja - data.total_sistema

            self.con.ping(reconnect=True)
            with self.con.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO cuadre_caja
                    (fecha, id_usuario, total_sistema, dinero_caja, diferencia, observacion)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    data.fecha,
                    data.id_usuario,
                    data.total_sistema,
                    data.dinero_caja,
                    diferencia,
                    data.observacion
                ))

                self.con.commit()

                return {
                    "success": True,
                    "message": "Cuadre de caja guardado correctamente",
                    "diferencia": diferencia
                }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

        finally:
            self.close_connection()

    def close_connection(self):
        if self.con:
            self.con.close()


    def obtener_ventas_online(self, fecha: str):
        try:
            self.con.ping(reconnect=True)
            with self.con.cursor(pymysql.cursors.DictCursor) as cursor:

                cursor.execute("""
                    SELECT
                        f.id_factura,
                        f.numero_factura,
                        f.total,
                        f.fecha,
                        f.id_usuario
                    FROM factura f
                    WHERE DATE(f.fecha) = %s
                      AND f.estado = 'emitida'
                      AND f.origen = 'online'
                """, (fecha,))

                ventas = cursor.fetchall()
                total_online = sum(v["total"] for v in ventas)

                return {
                    "success": True,
                    "ventas": ventas,
                    "total_online": total_online
                }

        except Exception as e:
            return {
                "success": False,
                "message": str(e)
            }

        finally:
            self.close_connection()

    def close_connection(self):
        if self.con:
            self.con.close()
