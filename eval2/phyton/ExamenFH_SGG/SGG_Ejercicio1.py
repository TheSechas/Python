
while True:
    numero = int(input("Indique un número entre 0 y 10: "))
    if numero >= 0 and numero <= 10:
        for i in range(10):
            print(f"{numero} x {i+1} = {numero * i + numero}")
        break
    else:
        print("El número no está dentro del rango permitido, inténtelo de nuevo.")
        


