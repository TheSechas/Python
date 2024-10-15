def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Solicitar al usuario que elija la conversión
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
opcion = input("Seleccione una opción (1 o 2): ")

if opcion == '1':
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
    else:
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
elif opcion == '2':
    try:
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    except ValueError:
        print("Por favor, ingrese un número válido.")
    else:
        celsius = fahrenheit_a_celsius(fahrenheit)
        print(f"{fahrenheit} grados Fahrenheit son equivalentes a {celsius} grados Celsius.")
else:
    print("Opción no válida. Por favor, seleccione 1 o 2.")
