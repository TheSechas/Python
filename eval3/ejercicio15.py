
producto = print("p. PRODUCTO")

resta = print("r. RESTA")

division = print("d. DIVISION")

salir = print("s. SALIR")

accion = str(input("SELECCIONE UNA OPCIÓN: "))

if accion == "p":
    producto = print("p. PRODUCTO")
    resta = print("r. RESTA")
    division = print("d. DIVISION")
    salir = print("s. SALIR")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado}")

if accion == "r":
    producto = print("p. PRODUCTO")
    resta = print("r. RESTA")
    division = print("d. DIVISION")
    salir = print("s. SALIR")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado}")

if accion == "d":
    producto = print("p. PRODUCTO")
    resta = print("r. RESTA")
    division = print("d. DIVISION")
    salir = print("s. SALIR")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división es: {resultado}")

if accion == "s":
    print("HASTA LUEGO")