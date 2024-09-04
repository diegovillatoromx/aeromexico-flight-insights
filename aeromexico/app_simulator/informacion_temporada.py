import datetime
import random 

# Fechas de vacaciones en México
vacaciones = [
    (datetime.datetime(2024, 7, 15), datetime.datetime(2024, 8, 15)),  # Verano
    (datetime.datetime(2024, 12, 15), datetime.datetime(2025, 1, 15)),  # Navidad
    (datetime.datetime(2024, 3, 25), datetime.datetime(2024, 4, 10)),  # Semana Santa
]

def es_temporada_alta(fecha):
    for inicio, fin in vacaciones:
        if inicio <= fecha <= fin:
            return True
    return False

def generar_informacion_completa(num_vuelos, informacion_vuelos, generar_informacion_financiera, generar_informacion_cliente, generar_informacion_operacional, generar_informacion_geografica):
    vuelos = informacion_vuelos(num_vuelos)
    informacion_completa = []
    for vuelo in vuelos:
        fecha = datetime.datetime.strptime(vuelo['fecha'], '%Y-%m-%d')
        temporada = 'alta' if es_temporada_alta(fecha) else 'baja'

        # Retrasos aleatorios cerca de la temporada alta
        if temporada == 'baja' and any(inicio - datetime.timedelta(days=7) <= fecha <= fin + datetime.timedelta(days=7) for inicio, fin in vacaciones):
            retraso_salida = random.randint(30, 90)
            retraso_llegada = random.randint(30, 90)
        else:
            retraso_salida = random.randint(0, 10)
            retraso_llegada = random.randint(0, 10)

        vuelo['hora_salida_real'] = f"{vuelo['hora_salida_programada'][:-2]}:{vuelo['hora_salida_programada'][-2:]}:{retraso_salida:02d}"
        vuelo['hora_llegada_real'] = f"{vuelo['hora_llegada_programada'][:-2]}:{vuelo['hora_llegada_programada'][-2:]}:{retraso_llegada:02d}"

        # Cambios en la demanda según temporadas
        if temporada == 'alta':
            num_pasajeros = random.randint(150, 200)
        else:
            num_pasajeros = random.randint(50, 100)

        vuelo['num_pasajeros'] = num_pasajeros

        informacion_vuelo = {
            'vuelo': vuelo,
            'informacion_financiera': generar_informacion_financiera(vuelo),
            'informacion_cliente': generar_informacion_cliente(),
            'informacion_operacional': generar_informacion_operacional(),
            'informacion_geografica': generar_informacion_geografica()
        }
        informacion_completa.append(informacion_vuelo)
    return informacion_completa
