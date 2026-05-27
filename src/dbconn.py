import psycopg2

def db_connection():
    conn = psycopg2.connect(
        dbname= 'clima_db',
        password='soporte',
        user='soporte'
    )

    return conn
