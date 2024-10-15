
precios = list()
articulos = list()

for i in range(10):
    precio = float(input(f"Introduce un precio para el Artículo {i+1}: "))
    articulo = str(input(f"Introduce el nombre del Artículo {i+1}: "))
    precios.append(precio)
    articulos.append(articulo)

precioMax = max(precios)
indicePrecioMax = precios.index(precioMax)
nombreArticuloMax = articulos[indicePrecioMax]

precioMin = min(precios)
indicePrecioMin = precios.index(precioMin)
nombreArticuloMin = articulos[indicePrecioMin]

precioMedio = sum(precios) / len(precios)

preciosDebajo30 = sum(1 for precio in precios if precio < 30)

print(f"El precio mayor es {precioMax} y su artículo es {nombreArticuloMax}")
print(f"El precio menor es {precioMin} y su artículo es {nombreArticuloMin}")
print(f"El precio promedio es {precioMedio}")
print(f"Número de precios por debajo de 30: {preciosDebajo30}")

