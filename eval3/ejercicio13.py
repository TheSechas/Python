numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

NIF = int(input("Escribe los 8 numeros de su NIF: "))

DNI = NIF % 23
indiceNumeros = numeros.index(DNI)
letraNIF = letras[indiceNumeros]

print(f"Su DNI es: {NIF} {letraNIF}")