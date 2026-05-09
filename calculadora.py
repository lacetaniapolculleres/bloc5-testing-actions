def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacio(a, b):
    return a * b

def divisio(a, b):
    if b == 0:
        raise ValueError('No es pot dividir per zero')
    return a / b
