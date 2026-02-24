#MRUA

def velocidad_final(velocidad_inicial, aceleracion, tiempo):
    velocidad_final = velocidad_inicial + aceleracion * tiempo
    return velocidad_final      

def distancia_recorrida(velocidad_inicial, aceleracion, tiempo):
    distancia = velocidad_inicial * tiempo + 0.5 * aceleracion * tiempo ** 2
    return distancia    



