# Inicializar listas para almacenar nombres y montos de gastos
categorias = []
montones = []

# Solicitar al usuario registrar los gastos mensuales de 10 categorías
for i in range(10):
    categoria = input(f"Ingrese el nombre de la categoría {i+1}: ")
    monton = float(input(f"Ingrese el monto gastado en la categoría {categoria}: "))
    categorias.append(categoria)
    montones.append(monton)

# Calcular el total gastado en todas las categorías
total_gastado = sum(montones)

# Encontrar la categoría con el gasto más alto y más bajo
indice_gasto_max = montones.index(max(montones))
indice_gasto_min = montones.index(min(montones))
categoria_max = categorias[indice_gasto_max]
categoria_min = categorias[indice_gasto_min]

# Calcular el promedio de gastos por categoría
promedio_gastos = total_gastado / len(categorias)

# Contar el número de categorías con un gasto menor a 100 dólares
num_categorias_menor_100 = sum(1 for monton in montones if monton < 100)

# Mostrar los resultados
print("\nResumen de gastos mensuales:")
print("Total gastado en todas las categorías:", total_gastado)
print("Categoría con el gasto más alto:", categoria_max)
print("Categoría con el gasto más bajo:", categoria_min)
print("Promedio de gastos por categoría:", promedio_gastos)
print("Número de categorías con un gasto menor a 100 dólares:", num_categorias_menor_100)

