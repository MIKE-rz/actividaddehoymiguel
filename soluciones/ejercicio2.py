'''
PLANTEAMIENTO DEL PROBLEMA
Calcular una aproximación de n! usando la fórmula de Stirling:
'''

# PROBLEMA: calcular una aproximación de n!
# ENTRADA: n
# SALIDA: resultado
# ALGORITMO
# 1. Leer n
# 2. Obtener el valor de pi usando math.pi
# 3. Obtener el valor de e usando math.e
# 4. Calcular n! usando la fórmula de Stirling
#    n! ≈ sqrt(2 * pi) * e**(-n) * n**(n + 1/2)
# 5. Mostrar el resultado


#CONTRATO DE FUNCIONES

#leerDatos()
#Entrada: ninguna
#Salida: n
#Responsabilidad: pedir el valor de n al usuario
#datos al usuario


#calcularFactorial(n)
#Entrada: n
#Salida: resultado
#Responsabilidad:
#calcular la aproximación de n!, no imprimir


#mostrarResultado(resultado)
#Entrada: resultado
#Salida: ninguna
#Responsabilidad:
#mostrar resultado


#CASOS DE PRUEBA
#Caso 1: n = 5
#Entrada: 5
#Salida: 118.019168
#
#Caso 2: n = 10
#Entrada: 10
#Salida: 3598695.618741
#
#Caso 3: n = 3
#Entrada: 3
#Salida: 5.836210


#Restricciones:
# - no imprimir dentro de la función calcularFactorial
# - devolver el resultado
# - usar la biblioteca math
# - usar math.sqrt()
# - usar math.e
# - usar math.pi
# - no usar variables globales
# - no realizar llamadas a funciones dentro de este archivo

def leerDatos():
    n = int(input("Ingrese un número entero positivo n: "))
    return n
def calcularFactorial(n):
    import math
    #resultado = math.sqrt(2 * math.pi * n) * (n / math.e) ** n
    resultado = math.sqrt(2 * math.pi) * (n / math.e) ** n * n ** 0.5
    return resultado
def mostrarResultado(resultado):
    print("La aproximación de n! es:", resultado)