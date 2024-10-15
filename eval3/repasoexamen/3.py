# Definimos una función para calcular la letra del NIF a partir del número del DNI.
def calcular_letra_nif(dni):
    # Tabla de letras según el resultado del módulo 23.
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    # Calculamos el índice dividiendo el número del DNI por 23 y tomando el resto.
    indice = dni % 23
    # Devolvemos la letra correspondiente al índice.
    return letras[indice]

# Definimos la función principal del programa.
def main():
    while True:  # Creamos un bucle infinito que continuará hasta que se introduzca un número válido.
        try:
            # Solicitamos al usuario que introduzca su número de DNI.
            dni = int(input("Introduce tu número de DNI (sin letra): "))
            # Verificamos que el número de DNI es positivo.
            if dni >= 0:
                # Calculamos la letra correspondiente al DNI.
                letra = calcular_letra_nif(dni)
                # Mostramos el NIF completo (DNI seguido de su letra).
                print(f"Tu NIF completo es: {dni}{letra}")
                break  # Salimos del bucle ya que el DNI es válido.
            else:
                # Mostramos un mensaje de error si el DNI no es positivo.
                print("El número de DNI debe ser un entero positivo.")
        except ValueError:
            # Mostramos un mensaje de error si la entrada no es un número entero.
            print("Por favor, introduce un número de DNI válido.")

# Verificamos si el script se está ejecutando directamente.
if __name__ == "__main__":
    # Llamamos a la función principal.
    main()
