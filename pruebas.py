def suma(a,b):
    return a + b



def promedio(lista):
    suma=0
    for i in lista:
        suma=suma + i
    return suma/len(lista)

def dividir(a,b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b
    
def calcular(a, operador, b):
    # Validar que el operador sea válido
    if operador not in ["+", "-", "*", "/"]:
        return "Operador no válido, inserte +, -, *, /"
    
    try:
        if operador == "+":
            return a+b
        elif operador == "-":
            return a-b  
        elif operador == "*":
            return a*b      
        elif operador == "/":
            return a/b
    except ZeroDivisionError as e:
        return "No se puede dividir por cero"
    except TypeError as e:
        return "Los operandos deben ser números"
    