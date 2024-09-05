import random
import json 

def generar_informacion_operacional():
    causas_de_retrasos = [
        'Tráfico aéreo',
        'Condiciones climáticas adversas',
        'Problemas técnicos en el avión',
        'Desvíos debido a emergencias médicas',
        'Desvíos debido a problemas de seguridad',
        'Retrasos en el abastecimiento de combustible',
        'Retrasos en el proceso de check-in',
        'Retrasos en el proceso de embarque',
        'Problemas con el equipo de tierra',
        'Colisiones con aves',
        'Otras causas'
    ]

    razones_de_cancelaciones = [
        'Mal tiempo',
        'Problemas técnicos en el avión',
        'Falta de pasajeros',
        'Desvíos debido a emergencias médicas',
        'Desvíos debido a problemas de seguridad',
        'Problemas con el personal de vuelo',
        'Problemas con el personal de tierra',
        'Problemas con el equipo de tierra',
        'Colisiones con aves',
        'Otras razones'
    ]

    distancia_de_ruta_minima = 500
    distancia_de_ruta_maxima = 10000

    # Determinar si hay retraso o cancelación
    hay_retraso = random.choice([True, False])
    hay_cancelacion = random.choice([True, False])

    informacion_operacional = {
        "retraso": {
            "causa": random.choice(causas_de_retrasos) if hay_retraso else "Ninguna",
            "duracion": random.randint(15, 120) if hay_retraso else 0
        },
        "cancelacion": {
            "razon": random.choice(razones_de_cancelaciones) if hay_cancelacion else "El cliente no se presentó"
        },
        "tasa_de_ocupacion": round(random.uniform(0.5, 1.0), 2),
        "distancia_de_ruta": random.randint(distancia_de_ruta_minima, distancia_de_ruta_maxima)
    }

    return json.dumps(informacion_operacional, indent=4)
