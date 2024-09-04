import pandas as pd
import random

# Datos de vuelos
vuelos = {
    'id': [i for i in range(1, 1001)],
    'origen': [random.choice(['MEX', 'GDL', 'MTY', 'CUN', 'TIJ']) for _ in range(1000)],
    'destino': [random.choice(['MEX', 'GDL', 'MTY', 'CUN', 'TIJ']) for _ in range(1000)],
    'fecha_hora_salida': [pd.to_datetime(f'2022-01-01 {random.randint(0, 23):02d}:{random.randint(0, 59):02d}') for _ in range(1000)],
    'fecha_hora_llegada': [pd.to_datetime(f'2022-01-01 {random.randint(0, 23):02d}:{random.randint(0, 59):02d}') for _ in range(1000)],
    'duracion_vuelo': [random.randint(1, 5) for _ in range(1000)],
    'numero_vuelo': [f'VUELO-{i}' for i in range(1, 1001)],
    'avion': [random.choice(['BOEING', 'AIRBUS', 'EMBRAER']) for _ in range(1000)],
    'capacidad_avion': [random.randint(100, 300) for _ in range(1000)],
    'pasajeros': [random.randint(50, 200) for _ in range(1000)],
    'carga': [random.randint(1000, 5000) for _ in range(1000)]
}

df_vuelos = pd.DataFrame(vuelos)
df_vuelos.to_csv('vuelos.csv', index=False)

# Datos de información financiera
informacion_financiera = {
    'id': [i for i in range(1, 1001)],
    'vuelo_id': [i for i in range(1, 1001)],
    'costo_combustible': [random.uniform(1000, 5000) for _ in range(1000)],
    'costos_mantenimiento': [random.uniform(500, 2000) for _ in range(1000)],
    'ingresos_venta_boletos': [random.uniform(5000, 20000) for _ in range(1000)],
    'ingresos_servicios_adicionales': [random.uniform(500, 2000) for _ in range(1000)],
    'costos_operativos': [random.uniform(1000, 5000) for _ in range(1000)]
}

df_informacion_financiera = pd.DataFrame(informacion_financiera)
df_informacion_financiera.to_csv('informacion_financiera.csv', index=False)

# Datos de información operacional
informacion_operacional = {
    'id': [i for i in range(1, 1001)],
    'vuelo_id': [i for i in range(1, 1001)],
    'retraso': [random.choice(['SI', 'NO']) for _ in range(1000)],
    'causa_retraso': [random.choice(['METEO', 'TECNICO', 'OPERATIVO']) for _ in range(1000)],
    'cancelacion': [random.choice(['SI', 'NO']) for _ in range(1000)],
    'razon_cancelacion': [random.choice(['METEO', 'TECNICO', 'OPERATIVO']) for _ in range(1000)],
    'tasa_ocupacion': [random.uniform(0.5, 1.0) for _ in range(1000)],
    'distancia_ruta': [random.randint(500, 2000) for _ in range(1000)]
}

df_informacion_operacional = pd.DataFrame(informacion_operacional)
df_informacion_operacional.to_csv('informacion_operacional.csv', index=False)