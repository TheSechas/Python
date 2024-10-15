# Pedir el número de alumnos por pantalla
num_alumnos = int(input("Ingrese el número de alumnos: "))

# Inicializar una lista para almacenar las notas de los alumnos
notas = []

# Leer las notas de cada alumno y almacenarlas en la lista
for i in range(num_alumnos):
    nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
    notas.append(nota)

# Calcular la media
suma_notas = sum(notas)
media = suma_notas / num_alumnos

# Calcular la nota máxima y mínima
nota_maxima = max(notas)
nota_minima = min(notas)

# Mostrar los resultados
print("\nResumen de notas:")
print("Nota media del curso:", media)
print("Nota máxima del curso:", nota_maxima)
print("Nota mínima del curso:", nota_minima)
