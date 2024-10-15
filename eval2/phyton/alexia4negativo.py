suma_numero = 0 
num = 0

num = int(input("introdua un numero: "))

if num > 0:
    for num2 in range(1, num + 1):
        suma_numero = suma_numero + num2
    print("el resultado es", suma_numero)
else:
    for num2 in range(1, -num + 1):
        suma_numero = suma_numero + num2
    print("el resultado es", -suma_numero)