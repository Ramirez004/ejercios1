def sucesion(n):
    return n + 1

def antecesor(n):
    return n - 1

def suma(a, b):
    if b == 0:
        return a
    else:
        return sucesion(suma(a, antecesor(b)))

def resta(a, b):
    if b < 0:
        return("Imposible realizar la operacion")
    if b == 0:
        return a
    else:
        return antecesor(resta(a, antecesor(b)))

def multiplicacion(a, b):
    if b == 0:
        return 0
    else:
        return suma(a, multiplicacion(a , antecesor(b)))

def division(a, b):
    if b == 0:
        return "!!Indefinido¡¡"
    if a < b:
        return 0
    else:
        return sucesion(division(resta(a, b), b))

print("Suma:", suma(3, 6))
print("Resta:", resta(-5, 5))
print("Multiplicación:", multiplicacion(5, 5))
print("División:", division(10, 3))
