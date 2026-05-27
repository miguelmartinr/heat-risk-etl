from extract import extract_data
from transform import transform_data
from dbconn import db_connection
from load import load_data

def init_etl():
    print('Iniciando ETL...')

    data = extract_data()
    print('Datos extraidos correctamente')

    data_trans = transform_data(data)
    print('Datos transformados con exito')

    conn = db_connection
    load_data(conn, transform_data)
    conn.close()

if __name__ == '__main__':
    init_etl()    