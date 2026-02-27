import pruebas

def test_suma():
    assert pruebas.suma(2, 3) == 5

def test_promedio():
    numeros = [1, 2, 3, 4, 5]
    assert pruebas.promedio(numeros) == 3.0 
    
def test_dividir():
    assert pruebas.dividir(10,5)==2
    assert pruebas.dividir(10,0)=="Error: No se puede dividir por cero"


