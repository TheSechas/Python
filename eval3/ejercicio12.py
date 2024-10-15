# Sumar los números pares e impares que se introduzcan por teclado, hasta que se teclee un valor
# menor que cero, en ese momento el programa finalizará mostrando la suma acumulada de pares e
# impares respecƟvamente

suma_pares = 0
suma_impares = 0

while True:
    numero = int(input("Ingrese un número entero (o un número negativo para salir): "))
    if numero < 0:
        break
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print(f"La suma acumulada de números pares es: {suma_pares}")
print(f"La suma acumulada de números impares es: {suma_impares}")
