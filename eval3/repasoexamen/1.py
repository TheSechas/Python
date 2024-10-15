# Define una función para sumar dos números
def suma(x, y):
    return x + y

# Define una función para restar dos números
def resta(x, y):
    return x - y

# Define una función para multiplicar dos números
def multiplicacion(x, y):
    return x * y

# Define una función para dividir dos números, verificando que el divisor no sea cero
def division(x, y):
    if y != 0:
        return x / y
    else:
        print("No se puede dividir un número entre 0.")
        return None

# Define la función principal del menú
def menu():
    while True:  # Inicia un bucle infinito que se ejecutará hasta que se elija la opción de salida
        # Imprime el menú de opciones
        print("\nMenú de opciones:")
        print("s. Suma")
        print("r. Resta")
        print("m. Multiplicacion")
        print("d. Division")
        print("e. Exit")

        # Solicita al usuario que seleccione una opción del menú
        opcion = input("Seleccione una opción del menú: ")

        # Dependiendo de la opción seleccionada, solicita los valores y realiza la operación correspondiente
        if opcion == "s":
            x = float(input("Seleccione el valor x: "))
            y = float(input("Seleccione el valor y: "))
            print("La Suma es:", suma(x, y))
        elif opcion == "r":
            x = float(input("Seleccione el valor x: "))
            y = float(input("Seleccione el valor y: "))
            print("La Resta es:", resta(x, y))
        elif opcion == "m":
            x = float(input("Seleccione el valor x: "))
            y = float(input("Seleccione el valor y: "))
            print("La Multiplicacion es:", multiplicacion(x, y))
        elif opcion == "d":
            x = float(input("Seleccione el valor x: "))
            y = float(input("Seleccione el valor y: "))
            division_resultado = division(x, y)
            if division_resultado is not None:
                print("La Division es:", division(x, y))
        elif opcion == "e":
            print("Hasta luego!")
            break  # Sale del bucle y termina el programa
        else:
            print("Opción no válida, inténtelo de nuevo.")

# Llama a la función del menú para iniciar el programa
menu()
