# Declarar un array de 10 números enteros
numeros = [0] * 10

# Solicitar al usuario la introducción de los elementos
for i in range(10):
    numeros[i] = int(input(f"Ingrese el elemento {i + 1}: "))

# Mostrar todos los elementos por pantalla
print("\nElementos del array:")
for numero in numeros:
    print(numero)
