import random
 
def generar_informacion_cliente():
    nacionalidades = ['Mexicana', 'Estadounidense', 'Canadiense', 'Europea', 'Asiática', 'Sudamericana']
    clases_de_vuelo = ['Económica', 'Ejecutiva', 'Primera clase']
    canales_de_venta = ['Agencia', 'Sitio web', 'Teléfono', 'Ventanilla']
    tipos_de_quejas = ['Retraso', 'Pérdida de equipaje', 'Servicio deficiente', 'Otros']

    informacion_cliente = {
        'nacionalidad': random.choice(nacionalidades),
        'clase_de_vuelo': random.choice(clases_de_vuelo),
        'frecuencia_de_vuelo': random.randint(1, 12),
        'canal_de_venta': random.choice(canales_de_venta),
        'satisfaccion_del_cliente': random.randint(1, 5),
        'queja': random.choice(tipos_de_quejas),
    }
    return informacion_cliente
