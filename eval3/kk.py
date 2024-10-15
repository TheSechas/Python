def ingresar_calificacion():
    while True:
        try:
            calificacion = float(input("Ingresa la calificación (0-100): "))
            if 0 <= calificacion <= 100:
                return calificacion
            else:
                print("Por favor, ingresa una calificación entre 0 y 100.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número.")

def determinar_estado(calificacion):
    if calificacion >= 60:
        return "Aprobado"
    else:
        return "Suspenso"

def main():
    while True:
        calificacion = ingresar_calificacion()
        estado = determinar_estado(calificacion)
        print(f"Calificación: {calificacion} - Estado: {estado}")

        continuar = input("¿Quieres ingresar otra calificación? (s/n): ").strip().lower()
        if continuar == "s":
            return main()
        if continuar == 'n':
            print("Gracias por usar el programa.")
            break
        else:
            print("Indique (s/n) ")

main()
