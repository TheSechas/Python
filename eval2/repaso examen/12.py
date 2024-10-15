# Solicitar al usuario el costo total de la comida
costo_total = float(input("Introduzca el costo total de la comida: "))

# Solicitar al usuario el porcentaje de propina que desea dejar
propina = float(input("Introduza la propina que desee dejar: "))

# Calcular la propina
monton_propina = costo_total * (propina / 100)

# Calcular el costo total de la comida más la propina
costo_total_mas_propina = costo_total + monton_propina

# Mostrar los resultados
print(f"El montón propina es de: {monton_propina} euros")
print(f"El costo total es de: {costo_total_mas_propina} euros")