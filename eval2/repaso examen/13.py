
Nombre = str(input("Indique su nombre: "))
Usuario = str(input("Usuario: "))

alutra = []
peso = []

if Nombre == "Sergio" and Usuario == "TheSechas":
    Contraseña = str(input("Contraseña: "))
else:
    print("Nombre de usuario incorrecto")

if Contraseña == "1234.Abcd":
    print("Bienvenido")

if Nombre == "Sergio" and Usuario == "TheSechas" and Contraseña == "1234.Abcd":
    alutra = float(input("Introduce tu altura: "))
    peso = float(input("Introduce tu peso: "))
    if alutra == 1.90 and peso == 72:
        print("Bienvenido, TheSechas")
    else:
        print("Tu altura o tu peso no son correctos")
