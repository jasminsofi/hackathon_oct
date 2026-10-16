AFORO_MAXIMO = 1.0

def validar_capacidad(capacidad, asistentes):
    return asistentes <= capacidad * AFORO_MAXIMO