# Solicitar al usuario un número entero
numero = int(input("Ingrese un número entero: "))

# Inicializar la variable para almacenar la suma
suma = 0

# Iterar desde 1 hasta el número ingresado (inclusive)
for i in range(1, numero + 1):
    # Sumar cada número al total
    suma += i

# Mostrar el resultado de la suma
print("La suma de los números hasta", numero, "es:", suma)
