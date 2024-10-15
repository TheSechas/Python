# Inicializar listas para almacenar los nombres y precios de los artículos
nombres = []
precios = []

# Solicitar al usuario los nombres y precios de los artículos
for i in range(10):
    nombre = input(f"Ingrese el nombre del artículo {i+1}: ")
    precio = float(input(f"Ingrese el precio del artículo {nombre}: "))
    nombres.append(nombre)
    precios.append(precio)

# Encontrar el índice del artículo con el precio más alto y más bajo
indice_max = precios.index(max(precios))
indice_min = precios.index(min(precios))

# Mostrar el nombre y precio del artículo más caro y más barato
print("\nArtículo con el precio más alto:")
print("Nombre:", nombres[indice_max])
print("Precio:", precios[indice_max])

print("\nArtículo con el precio más bajo:")
print("Nombre:", nombres[indice_min])
print("Precio:", precios[indice_min])

# Calcular el precio medio de los artículos
precio_medio = sum(precios) / len(precios)

# Mostrar el precio medio de los artículos
print("\nPrecio medio de los artículos:", precio_medio)

# Contar el número de precios por debajo de 30 euros
precios_debajo_30 = sum(1 for precio in precios if precio < 30)

# Mostrar el número de precios por debajo de 30 euros
print("Número de precios por debajo de 30 euros:", precios_debajo_30)
