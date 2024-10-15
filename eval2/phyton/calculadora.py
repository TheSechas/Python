def suma(x, y):
    return x + y

def resta(x, y):
    return x - y

def multiplicacion(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "No se puede dividir por cero."

while True:
    # Solicitar al usuario la operación deseada
    print("\nOperaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")

    opcion = input("Seleccione una operación (1/2/3/4/5): ")

    # Verificar la opción seleccionada
    if opcion == "5":
        print("¡Hasta luego!")
        break
    elif opcion in ("1", "2", "3", "4"):
        # Solicitar al usuario dos números
        numero1 = float(input("Ingrese el primer número: "))
        numero2 = float(input("Ingrese el segundo número: "))

        # Realizar la operación seleccionada
        if opcion == "1":
            resultado = suma(numero1, numero2)
            print(f"Resultado: {resultado}")
        elif opcion == "2":
            resultado = resta(numero1, numero2)
            print(f"Resultado: {resultado}")
        elif opcion == "3":
            resultado = multiplicacion(numero1, numero2)
            print(f"Resultado: {resultado}")
        elif opcion == "4":
            resultado = division(numero1, numero2)
            print(f"Resultado: {resultado}")
        else:
            print("Opción no válida. Inténtelo de nuevo.")
    else:
        print("Opción no válida. Inténtelo de nuevo.")
