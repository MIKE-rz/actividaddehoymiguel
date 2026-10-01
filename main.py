from soluciones.salario_semanal import calcularSalario, mostrarSalario, leerDatos

def main():

    horas, pago = leerDatos()
    salario = calcularSalario(horas, pago)
    mostrarSalario(salario)

if __name__ == "__main__":
    main()
