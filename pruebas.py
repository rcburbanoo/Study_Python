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
    
