'''
PLANTEAMIENTO DEL PROBLEMA
Calcula el valor de x usando la fórmula: x = sqrt(b - a**2) / c
'''

# PROBLEMA: calcular x
# ENTRADAS: a, b, c
# SALIDA: x
# ALGORITMO
# 1. Leer a
# 2. Leer b
# 3. Leer c
# 4. Calcular x
#    x = sqrt(b - a**2) / c
# 5. Mostrar x


#CONTRATO DE FUNCIONES

#leerDatos()
#Entrada: ninguna
#Salida: a, b y c
#Responsabilidad: pedir datos al usuario
#datos al usuario


#calcularX(a, b, c)
#Entrada: a, b y c
#Salida: x
#Responsabilidad:
#calcular, no imprimir


#mostrarResultado(x)
#Entrada: x
#Salida: ninguna
#Responsabilidad:
#mostrar resultado


#CASOS DE PRUEBA
#Caso 1: a = 2, b = 20, c = 5
#Entrada: 2, 20, 5
#Salida: 0.8
#
#Caso 2: a = 3, b = 25, c = 4
#Entrada: 3, 25, 4
#Salida: 1.0
#
#Caso 3: a = 1, b = 10, c = 3
#Entrada: 1, 10, 3
#Salida: 1.0


#Restricciones:
# - no imprimir dentro de la función calcularX
# - devolver el resultado
# - usar la biblioteca math
# - usar math.sqrt()
# - no usar variables globales
# - no realizar llamadas a funciones dentro de este archivo
def leerDatos():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    return a, b, c
def calcularX(a, b, c):
    import math
    x = math.sqrt(b - a**2) / c
    return x
def mostrarResultado(x):
    print("El valor de x es:", x)