# Heat Risk ETL Python - Postgres


Pipeline ETL que obtiene datos de OpenWeather, calcula un índice de riesgo de calor y los almacena en PostgreSQL.

La arquitectura del pipeline se resume en:

Extracción: a través de una función en python y la librería requests, se extraen los datos de, en principio, la ciudad de Madrid. Estos datos se guardan en un archivo JSON para futuras consultas con la librería json, además de crear un diccionario de python con ellos para continuar la ETL.
Transformación: gracias a este diccionario que hemos guardado, se puede crear la función para transformar los datos extraidos y crear la métrica de índice de riesgo.
Conexión: se define una función muy sencilla para poder conectar python a la base de datos de psotgres, utilizando la libreria psycopg2.
Carga: se crean funciones gracias a psycopg2 donde se crean aqui en python las tablas necesarias y se añaden los datos transformados y guardados en el diccionario.

