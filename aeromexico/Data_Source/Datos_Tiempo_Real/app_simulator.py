import json
import time 
from informacion_vuelos import generar_vuelo, informacion_vuelos
from informacion_financiera import generar_informacion_financiera
from informacion_clientes import generar_informacion_cliente
from informacion_operacional import generar_informacion_operacional
from informacion_geografica import generar_informacion_geografica
from informacion_temporada import generar_informacion_completa as generar_informacion_completa_temporada

def generar_informacion_completa(num_vuelos):
    informacion_completa = generar_informacion_completa_temporada(
        num_vuelos,
        informacion_vuelos,
        generar_informacion_financiera,
        generar_informacion_cliente,
        generar_informacion_operacional,
        generar_informacion_geografica
    )
    return json.dumps(informacion_completa, indent=4)
