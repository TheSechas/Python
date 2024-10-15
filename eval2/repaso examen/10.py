
# Solicitar al usuario su peso en kilogramos y su altura en metros
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (altura ** 2)

# Mostrar el IMC
print("Su índice de masa corporal (IMC) es:", imc)

# Mostrar un mensaje sobre el estado del peso según el IMC
if imc < 18.5:
    print("Tiene un peso inferior al recomendado.")
elif 18.5 <= imc < 25:
    print("Tiene un peso dentro del rango saludable.")
else:
    print("Tiene un peso superior al recomendado.")
