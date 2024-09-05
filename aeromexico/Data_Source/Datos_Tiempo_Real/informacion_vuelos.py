import random
import datetime 

def generar_aeropuerto(tipo):
    aeropuertos_nacionales = ['MEX', 'GDL', 'MTY', 'CUN', 'TIJ', 'SLP', 'AGU', 'BJX', 'ACA', 'VER']
    aeropuertos_internacionales = ['LAX', 'JFK', 'LHR', 'CDG', 'FRA', 'AMS', 'HKG', 'NRT', 'SYD', 'BUE']
    if tipo == 'nacional':
        return random.choice(aeropuertos_nacionales)
    else:
        return random.choice(aeropuertos_internacionales)

def generar_avion():
    aviones = {
        'Boeing 737-800': 189,
        'Airbus A320': 180,
        'Boeing 787-9': 290,
        'Airbus A330-200': 295
    }
    modelo, capacidad = random.choice(list(aviones.items()))
    return {'modelo': modelo, 'capacidad': capacidad}

def generar_fecha_hora():
    fecha = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 365))
    hora = random.randint(0, 23)
    minuto = random.randint(0, 59)
    return fecha.strftime("%Y-%m-%d"), f"{hora:02d}:{minuto:02d}"

def generar_fecha_hora_llegada(fecha_salida, hora_salida, duracion_estimada):
    fecha_salida_obj = datetime.datetime.strptime(f"{fecha_salida} {hora_salida}", "%Y-%m-%d %H:%M")
    fecha_llegada_obj = fecha_salida_obj + datetime.timedelta(hours=duracion_estimada)
    return fecha_llegada_obj.strftime("%Y-%m-%d"), fecha_llegada_obj.strftime("%H:%M")

def generar_vuelo():
    origen = generar_aeropuerto('nacional' if random.random() < 0.7 else 'internacional')
    destino = generar_aeropuerto('nacional' if random.random() < 0.7 else 'internacional')
    while origen == destino:
        destino = generar_aeropuerto('nacional' if random.random() < 0.7 else 'internacional')
    avion = generar_avion()
    fecha_salida, hora_salida = generar_fecha_hora()
    duracion_estimada = random.randint(1, 12)  # En horas
    fecha_llegada, hora_llegada = generar_fecha_hora_llegada(fecha_salida, hora_salida, duracion_estimada)
    duracion_real = duracion_estimada + random.randint(-2, 2)  # Simula retrasos o adelantos
    numero_vuelo = f"VU{random.randint(1000, 9999)}"

    vuelo = {
        'origen': origen,
        'destino': destino,
        'fecha_salida_programada': fecha_salida,
        'hora_salida_programada': hora_salida,
        'fecha_llegada_programada': fecha_llegada,
        'hora_llegada_programada': hora_llegada,
        'fecha_salida_real': fecha_salida,
        'hora_salida_real': hora_salida,
        'fecha_llegada_real': fecha_llegada,
        'hora_llegada_real': hora_llegada,
        'duracion_estimada': duracion_estimada,
        'duracion_real': duracion_real,
        'numero_vuelo': numero_vuelo,
        'avion': avion['modelo'],
        'capacidad_avion': avion['capacidad'],
        'pasajeros': random.randint(0, avion['capacidad']),
        'carga': random.randint(1000, 10000),
    }
    return vuelo

def informacion_vuelos(num_vuelos):
    vuelos = []
    for _ in range(num_vuelos):
        vuelos.append(generar_vuelo())
    return vuelos
