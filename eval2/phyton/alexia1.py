numPar = 0
resp = "S"

while resp == "S" or resp == "s":
    numPar = int(input("Ingrese un número: "))

    if numPar % 2 == 0:
        print("El número es par")
    elif numPar % 2 == 1:
        print("El número es impar")

    resp = str(input("¿Quieres repetir otra vez? (S/N) : "))