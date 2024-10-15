# Inicializa una lista vacía llamada lista1
lista1 = list()

# Define una función para solicitar una lista de números al usuario
def solicitar_lista():
    fin = 0  # Variable para controlar el fin del bucle
    numero = 0  # Variable para almacenar los números introducidos por el usuario
    lista = list()  # Inicializa una lista vacía para almacenar los números introducidos
    print(f"Introduce números hasta teclear un carácter no numérico.")
    while fin == 0:  # Inicia un bucle que continuará hasta que fin sea diferente de 0
        try:
            # Intenta convertir la entrada del usuario a un entero
            numero = int(input("Introduce número:"))
            # Si la conversión tiene éxito, añade el número a la lista
            lista.append(numero)
        except ValueError:
            # Si se produce una excepción ValueError (es decir, el usuario introduce un valor no numérico),
            # establece fin a 1 para terminar el bucle
            fin = 1
    # Devuelve la lista de números introducidos por el usuario
    return lista

# Define una función para calcular la moda de una lista de números
def calcula_moda(lista):
    cont = 0  # Variable temporal para iterar sobre los elementos de la lista
    frecu = 0  # Variable para almacenar la frecuencia máxima encontrada
    # Recorre cada número en la lista
    for cont in lista:
        # Si la frecuencia actual del número es mayor que la frecuencia máxima encontrada,
        # actualiza la frecuencia máxima y guarda el número como moda
        if frecu < lista.count(cont):
            frecu = lista.count(cont)
            moda = cont
    # Devuelve la moda
    return moda

# Llama a la función solicitar_lista y almacena la lista resultante en lista1
lista1 = solicitar_lista()
# Calcula la moda de lista1 y la imprime
print(f"La moda de lista1 es: {calcula_moda(lista1)}")
