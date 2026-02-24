import funciones_fisica

def test_vfinal():
    assert funciones_fisica.velocidad_final(0, 10, 2) == 20
    
    
def test_distancia():
    assert funciones_fisica.distancia_recorrida(0, 10, 3) == 45
