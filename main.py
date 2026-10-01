from soluciones.salario_semanal import calcularSalario, mostrarSalario, leerDatos
from soluciones.ejercicio1 import calcularX, mostrarResultado, leerDatos as leerDatosEj1
from soluciones.ejercicio2 import calcularFactorial, mostrarResultado as mostrarResultadoEj2, leerDatos as leerDatosEj2

def main():
    while True:
        print("Menú de opciones:")
        print("1. Calcular salario")
        print("2. Calcular x")
        print("3. Calcular n factorial")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            horas, pago = leerDatos()
            salario = calcularSalario(horas, pago)
            mostrarSalario(salario)
        if opcion == "2":
            a, b, c = leerDatosEj1()
            x = calcularX(a, b, c)
            mostrarResultado(x)
        if opcion == "3":
            n = leerDatosEj2()
            resultado = calcularFactorial(n)
            mostrarResultado(resultado)
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
