# Solicitar al usuario un número entre 0 y 10
while True:
    numero = int(input("Ingrese un número entre 0 y 10: "))
    if 0 <= numero <= 10:
        break
    else:
            print("Error: El número no está en el rango permitido (0-10). Inténtelo nuevamente.")

# Mostrar la tabla de multiplicar si el número cumple la condición
print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

