# Función para solicitar una lista de números al usuario
def solicitar_lista():
    lista = []  # Inicializa una lista vacía
    print("Introduce números hasta teclear un carácter no numérico.")
    while True:  # Inicia un bucle infinito
        try:
            numero = int(input("Introduce número: "))  # Solicita un número al usuario
            lista.append(numero)  # Añade el número a la lista
        except ValueError:  # Si el usuario introduce un valor no numérico, se rompe el bucle
            break
    return lista  # Devuelve la lista de números introducidos

# Función para calcular la moda de una lista de números
def calcula_moda(lista):
    if not lista:  # Verifica si la lista está vacía
        return None

    frecuencias = {}  # Inicializa un diccionario para contar las frecuencias
    for numero in lista:  # Recorre cada número en la lista
        if numero in frecuencias:  # Si el número ya está en el diccionario, incrementa su contador
            frecuencias[numero] += 1
        else:  # Si el número no está en el diccionario, lo añade con un contador inicial de 1
            frecuencias[numero] = 1

    # Encuentra el número con la mayor frecuencia
    moda = max(frecuencias, key=frecuencias.get)
    return moda  # Devuelve la moda

# Solicita al usuario una lista de números
lista1 = solicitar_lista()
# Calcula la moda de la lista
moda = calcula_moda(lista1)

# Muestra el resultado
if moda is not None:
    print(f"La moda de lista1 es: {moda}")
else:
    print("La lista está vacía, no hay moda.")

