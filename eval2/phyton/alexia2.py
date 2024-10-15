num = 0

while True:
    num = int(input("Introduce un número entre 0 y 10: "))
    if num >= 0 and num <= 10:
        print("Tabla de multiplicar de", num)
        for i in range(1, 11):
            print(num, "x", i, "=", num * i)
    else:
        print("El número no está entre 0 y 10. Inténtalo de nuevo.")
