# Solicitar al usuario dos números
numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

# Realizar operaciones matemáticas
suma = numero1 + numero2
resta = numero1 - numero2
producto = numero1 * numero2

# Mostrar los resultados
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Producto: {producto}")

# Verificar si el segundo número es diferente de cero antes de realizar la división
if numero2 != 0:
    division = numero1 / numero2
    print(f"División: {division}")
else:
    print("No se puede dividir por cero.")

# Utilizar un bucle while para contar hasta el segundo número
contador = 0
while contador <= numero2:
    print(f"Contador: {contador}")
    contador += 1
