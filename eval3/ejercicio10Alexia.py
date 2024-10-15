# Realiza un programa que nos muestre los números de 1 a N (introducido por pantalla). Nos deberá
# indicar cuántos pares hay y cuáles, cuántos impares hay y cuáles. Por úlƟmo deberá mostrar la
# media aritméƟca de pares y de impares.

Par = list()
Impar = list()
suma_pares = 0
suma_impares = 0

indicaNumero = int(input("Indique cuantos números quiere almacenar: "))

for i in range(1, indicaNumero + 1):
    if i % 2 == 0:
        Par.append(i)
        suma_pares += i
    else:
        Impar.append(i)
        suma_impares += i

totalPar = len(Par)
totlaImpar = len(Impar)

media_pares = suma_pares / totalPar if totalPar != 0 else 0
media_impares = suma_impares / totlaImpar if totlaImpar != 0 else 0

print(f"Números pares: {Par}")
print(f"Números impares: {Impar}")
print(f"Total de pares: {totalPar}")
print(f"Total de impares: {totlaImpar}")
print(f"Media de pares: {media_pares}")
print(f"Media de impares: {media_impares}")