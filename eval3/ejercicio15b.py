def mostrar_menu():
    print("p. PRODUCTO")
    print("r. RESTA")
    print("d. DIVISION")
    print("s. SALIR")

def obtener_accion():
    while True:
        accion = input("SELECCIONE UNA OPCIÓN: ").lower()
        if accion in ['p', 'r', 'd', 's']:
            return accion
        else:
            print("Opción inválida. Por favor, seleccione nuevamente.")

def obtener_numeros():
    while True:
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            return num1, num2
        except ValueError:
            print("Por favor, ingrese números válidos.")

def realizar_operacion(accion, num1, num2):
    if accion == 'p':
        return num1 * num2
    elif accion == 'r':
        return num1 - num2
    elif accion == 'd':
        try:
            return num1 / num2
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
            return None

def calculadora():
    while True:
        mostrar_menu()
        accion = obtener_accion()

        if accion == 's':
            print("HASTA LUEGO")
            break

        num1, num2 = obtener_numeros()
        resultado = realizar_operacion(accion, num1, num2)
        
        if resultado is not None:
            print(f"El resultado es: {resultado}")

calculadora()

