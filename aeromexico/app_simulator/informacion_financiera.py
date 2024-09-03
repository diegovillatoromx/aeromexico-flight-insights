import random

def generar_informacion_financiera(vuelo):
    costo_combustible_por_litro = random.uniform(0.5, 1.5)
    costo_combustible_por_vuelo = costo_combustible_por_litro * random.randint(1000, 5000)
    costo_mantenimiento_por_avion = random.uniform(500, 2000)
    costo_mantenimiento_por_hora = costo_mantenimiento_por_avion / vuelo['duracion_estimada']
    ingresos_boletos_economicos = random.randint(500, 1000) * random.randint(50, 100)
    ingresos_boletos_ejecutivos = random.randint(1000, 2000) * random.randint(20, 50)
    ingresos_servicios_adicionales = random.randint(1000, 2000)
    costos_operativos = random.uniform(5000, 10000)

    informacion_financiera = {
        'costo_combustible_por_vuelo': round(costo_combustible_por_vuelo, 2),
        'costo_combustible_por_litro': round(costo_combustible_por_litro, 2),
        'costo_mantenimiento_por_avion': round(costo_mantenimiento_por_avion, 2),
        'costo_mantenimiento_por_hora': round(costo_mantenimiento_por_hora, 2),
        'ingresos_boletos_economicos': ingresos_boletos_economicos,
        'ingresos_boletos_ejecutivos': ingresos_boletos_ejecutivos,
        'ingresos_servicios_adicionales': ingresos_servicios_adicionales,
        'costos_operativos': round(costos_operativos, 2),
    }
    return informacion_financiera

vuelo = {
    'duracion_estimada': 5,  # Horas
}