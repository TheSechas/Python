def producto(x, y):
    return x * y

def resta(x, y):
    return x - y

def division(x, y):
    if y != 0:
        return x / y
    else:
        print("Error: No se puede dividir por cero.")
        return None

def menu():
    while True:
        # Mostrar el menú de opciones
        print("\nMenú de opciones:")
        print("p.- Producto (x,y)")
        print("r.- Resta (x,y)")
        print("d.- División (x,y)")
        print("s.- Salir")

        # Solicitar al usuario que seleccione una opción
        opcion = input("Seleccione una opción del menú: ")

        # Verificar la opción seleccionada
        if opcion == 'p':
            x = float(input("Ingrese el primer número (x): "))
            y = float(input("Ingrese el segundo número (y): "))
            print("Producto:", producto(x, y))
        elif opcion == 'r':
            x = float(input("Ingrese el primer número (x): "))
            y = float(input("Ingrese el segundo número (y): "))
            print("Resta:", resta(x, y))
        elif opcion == 'd':
            x = float(input("Ingrese el primer número (x): "))
            y = float(input("Ingrese el segundo número (y): "))
            print("División:", division(x, y))
        elif opcion == 's':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida del menú.")

# Llamar a la función del menú
menu()
