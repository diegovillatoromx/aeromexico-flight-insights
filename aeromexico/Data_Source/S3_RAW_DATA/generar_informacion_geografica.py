import pandas as pd
import random

# Coordenadas reales de los aeropuertos
aeropuertos = {
    'MEX': {'latitud': 19.4363, 'longitud': -99.0721},
    'GDL': {'latitud': 20.5225, 'longitud': -103.3097},
    'MTY': {'latitud': 25.7854, 'longitud': -100.1077},
    'CUN': {'latitud': 21.0365, 'longitud': -86.8769},
    'TIJ': {'latitud': 32.5362, 'longitud': -117.0203},
    'SLP': {'latitud': 22.1536, 'longitud': -100.9267},
    'AGU': {'latitud': 21.7025, 'longitud': -102.8639},
    'BJX': {'latitud': 20.9942, 'longitud': -101.4797},
    'ACA': {'latitud': 16.7658, 'longitud': -99.7639},
    'VER': {'latitud': 19.1433, 'longitud': -96.1733},
    'LAX': {'latitud': 33.9425, 'longitud': -118.4070},
    'JFK': {'latitud': 40.6397, 'longitud': -73.7789},
    'LHR': {'latitud': 51.4700, 'longitud': -0.4543},
    'CDG': {'latitud': 49.0128, 'longitud': 2.5489},
    'FRA': {'latitud': 50.0333, 'longitud': 8.5705},
    'AMS': {'latitud': 52.3105, 'longitud': 4.7683},
    'HKG': {'latitud': 22.3080, 'longitud': 113.9154},
    'NRT': {'latitud': 35.7647, 'longitud': 140.3864},
    'SYD': {'latitud': -33.9461, 'longitud': 151.1771},
    'BUE': {'latitud': -34.6037, 'longitud': -58.3711},
}

def generar_informacion_geografica():
    aeropuerto_origen = random.choice(list(aeropuertos.keys()))
    aeropuerto_destino = random.choice(list(aeropuertos.keys()))
    while aeropuerto_destino == aeropuerto_origen:
        aeropuerto_destino = random.choice(list(aeropuertos.keys()))

    distancia_entre_aeropuertos = random.randint(500, 10000)

    informacion_geografica = {
        'aeropuerto_origen': aeropuertos[aeropuerto_origen],
        'aeropuerto_destino': aeropuertos[aeropuerto_destino],
        'distancia_entre_aeropuertos': distancia_entre_aeropuertos
    }
    return informacion_geografica

# Información geográfica
aeropuertos_info = []
for i in range(10000):
    aeropuerto_info = generar_informacion_geografica()
    aeropuertos_info.append(aeropuerto_info)

df_aeropuertos = pd.DataFrame(aeropuertos_info)
df_aeropuertos.to_csv("informacion_geografica.csv", index=False)