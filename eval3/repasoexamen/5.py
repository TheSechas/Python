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
        print("¡Error! No se puede dividir por cero.")
        return None

# Solicita al usuario que ingrese dos números
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
except ValueError:
    print("¡Error! Debes ingresar números válidos.")
else:
    # Calcula y muestra la suma, resta, multiplicación y división de los números
    print(f"\nSuma: {suma(num1, num2)}")
    print(f"Resta: {resta(num1, num2)}")
    print(f"Multiplicación: {multiplicacion(num1, num2)}")
    division_resultado = division(num1, num2)
    if division_resultado is not None:
        print(f"División: {division_resultado}")
