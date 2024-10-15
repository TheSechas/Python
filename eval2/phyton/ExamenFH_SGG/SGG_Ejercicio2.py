
numeros = []

for i in range(10):
    numero = int(input(f"Introduzca el número {i+1}: "))
    numeros.append(numero)

for i in reversed(numeros):
    print(i)