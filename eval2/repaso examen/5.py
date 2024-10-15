# Solicitar al usuario el límite inferior y superior del intervalo
limite_inferior = int(input("Ingrese el límite inferior del intervalo: "))
limite_superior = int(input("Ingrese el límite superior del intervalo: "))

# Verificar si el límite inferior es mayor que el límite superior, en cuyo caso, intercambiar los valores
if limite_inferior > limite_superior:
    limite_inferior, limite_superior = limite_superior, limite_inferior

# Imprimir los números impares en el intervalo
print("\nNúmeros impares en el intervalo de", limite_inferior, "a", limite_superior, ":")

for num in range(limite_inferior, limite_superior + 1):
    if num % 2 != 0:
        print(num)

