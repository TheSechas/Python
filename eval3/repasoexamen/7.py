def es_primo(numero):
    if numero <= 1:
        return False  # Los números menores o iguales a 1 no son primos

    # Comprobar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False  # Si es divisible, no es primo
    return True  # Si no es divisible por ningún número, es primo

# Solicitar al usuario que ingrese un número
try:
    num = int(input("Ingrese un número entero positivo mayor que 1: "))
except ValueError:
    print("Por favor, ingrese un número entero válido.")
else:
    if num <= 1:
        print("El número debe ser mayor que 1.")
    else:
        if es_primo(num):
            print(f"{num} es un número primo.")
        else:
            print(f"{num} no es un número primo.")
