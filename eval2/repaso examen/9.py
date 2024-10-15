
articulos = 10
nombre_articulo = []
precio_articulo = []

for i in range(articulos):
    articulo = (input(f"Indique el nombre del articulo {i+1}: "))
    precio = float(input(f"Indique el precio del articulo {articulo}: "))
    precio_articulo.append(precio)
    nombre_articulo.append(articulo)

precio_mayor = precio_articulo.index(max(precio_articulo))
precio_menor = precio_articulo.index(min(precio_articulo))

precio_medio = sum(precio_articulo) / articulos

precio_debajo30 = sum(1 for precio in precio_articulo if precio < 30)

print("\nArtículo con mayor precio:")
print("Nombre:", nombre_articulo[precio_mayor])
print("Precio:", precio_articulo[precio_mayor], "euros")


print("\nArtículo con menor precio:")
print("Nombre:", nombre_articulo[precio_menor])
print("Precio:", precio_articulo[precio_menor], "euros")

print("\nPrecio medio de los artículos:", precio_medio, "euros")

print("\nNúmero de artículos con precio menor a 30 euros:", precio_debajo30)