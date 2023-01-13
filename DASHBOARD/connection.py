import psycopg2
import settings
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def conectar():
    conn = psycopg2.connect(database=settings.DATABASE,
                            user=settings.USER,
                            password=settings.PASSWORD,
                            host=settings.HOST,
                            port=settings.PORT)

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()
    return cur, conn

def cerrar(conn,cur):
    cur.close()
    conn.close()