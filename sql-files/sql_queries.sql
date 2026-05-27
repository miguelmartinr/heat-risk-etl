--  Table creation

CREATE TABLE IF NOT EXISTS clima(
    id SERIAL PRIMARY KEY,
    ciudad VARCHAR(50),
    temp FLOAT,
    humedad INT,
    viento FLOAT,
    sensacion FLOAT,
    IRC FLOAT,
    fecha TIMESTAMP DEFAULT NOW()
);


-- Data inseted from .py
INSERT INTO clima(
    ciudad,
    temp,
    humedad,
    viento,
    sensacion,
    IRC) 
VALUES(%s, %s, %s, %s, %s, %s),
(
temp_madrid['ciudad'],
temp_madrid['temperatura'],
temp_madrid['humedad'],
temp_madrid['viento'],
temp_madrid['sensacion_termica'],
temp_madrid['IRC']
);


