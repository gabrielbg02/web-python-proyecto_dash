while True:
    try:
        print("MENU")
        print("1-SUMAR")
        print("2-RESTAR")
        print("3-MULTIPLICAR")
        print("4-DIVIDIR")
        print("0-SALIR")
        opcion = int(input("Opción a elegir: "))

        if opcion == 0:
            break  # Salir del bucle

        if 1 <= opcion <= 4:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))

            if opcion == 1:
                resultado = num1 + num2
            elif opcion == 2:
                resultado = num1 - num2
            elif opcion == 3:
                resultado = num1 * num2
            else:
                if num2 == 0:
                    print("No se puede dividir por cero")
                else:
                    resultado = num1 / num2

            print("Resultado:", resultado)
        else:
            print("Opción inválida")

    except ValueError:
        print("Ingrese una opción válida")