import pruebas

def test_suma():
    assert pruebas.suma(2, 3) == 5

def test_promedio():
    numeros = [1, 2, 3, 4, 5]
    assert pruebas.promedio(numeros) == 3.0 
    
def test_dividir():
    assert pruebas.dividir(10,5)==2
    assert pruebas.dividir(10,0)=="Error: No se puede dividir por cero"
    
def test_calcular():
    assert pruebas.calcular(10, "+", 5) == 15
    assert pruebas.calcular(10, "-", 5) == 5
    assert pruebas.calcular(10, "*", 5) == 50
    assert pruebas.calcular(10, "/", 5) == 2
    assert pruebas.calcular(10, "/", 0) == "No se puede dividir por cero"
    assert pruebas.calcular(10, "^", 5) == "Operador no válido, inserte +, -, *, /"
    assert pruebas.calcular("10", "+", 5) == "Los operandos deben ser números"


