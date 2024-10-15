# Inicializar una lista para almacenar los números
numeros = []

# Leer los números del usuario y almacenarlos en la lista
for i in range(10):
    numero = int(input(f"Ingrese el número {i + 1}: "))
    numeros.append(numero)

# Mostrar los números en orden inverso al de su introducción
print("\nNúmeros en orden inverso:")
for numero in reversed(numeros):
    print(numero)
