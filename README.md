# ejercios1

# Operaciones Básicas con Función Sucesora y Antecesora en Python

Este repositorio contiene una implementación en Python de las operaciones básicas (suma, resta, multiplicación y división) utilizando únicamente las funciones sucesora
(S(n) = n +1) y antecesora (A(n) = n-1), sin emplear operadores aritméticos directos

Funciones Implementadas

Sucesor
def sucesion(n):
    return n + 1
  Devuelve el número siguiente a n

Antecesor
def antecesor(n):
    return n - 1
  Devuelve el número anterior a n

Suma
def suma(a, b):
    if b == 0:
        return a
    else:
        return sucesion(suma(a, antecesor(b)))
  Realiza la suma de a y b unicamente con la funcion sucesora

Resta
def resta(a, b):
    if b < 0:
        return("Imposible realizar la operacion")
    if b == 0:
        return a
    else:
        return antecesor(resta(a, antecesor(b)))
  Calcula a - b pero no admite valores negativos en b

Multiplicacion  
def multiplicacion(a, b):
    if b == 0:
        return 0
    else:
        return suma(a, multiplicacion(a, antecesor(b)))
  Suma a consigo mismo b veces 

Division
def division(a, b):
    if b == 0:
        return "!!Indefinido¡¡"
    if a < b:
        return 0
    else:
        return sucesion(division(resta(a, b), b))
  
Realiza la división entera de a / b, evolviendo únicamente el cociente porque en la funcion sucesora se maneja numeros naturales



  
