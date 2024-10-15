
numeros = []

for i in range(10):
    numero = int(input(f"Introduce el número {i+1}: "))
    numeros.append(numero)

numero_mas = int(input("Introduce el número para adivinar: "))

repite = numeros.count(numero_mas)

print(f"El número {numero_mas} se repite {repite} veces ")