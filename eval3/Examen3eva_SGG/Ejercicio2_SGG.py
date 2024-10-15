def circulo(radio):
    return 3.1416 * (radio * radio)

def rectangulo(base, altura):
    return base * altura

def triangulo(base, altura):
    return base * altura * 1/2

def menu():
    while True:
        print("1.- Calcular área de un círculo")
        print("2.- Calcular área de un rectángulo")
        print("3.- Calcular área de un triángulo")
        print("4.- Salir.")

        opcion = int(input("Selecione lo que desee calcular(1, 2, 3, 4): "))
        
        if opcion == 1:
            radio = float(input("Indique el radio del circulo: "))
            print("El área del circulo es", circulo(radio))
        if opcion == 2:
            base = float(input("Indique la base del rectángulo: "))
            altura = float(input("Indique la altura del rectángulo: "))
            print("El área del rectángulo es", rectangulo(base, altura))
        if opcion == 3:
            base = float(input("Indique la base del triángulo: "))
            altura = float(input("Indique la altura del triángulo: "))
            print("El área del triángulo es", triangulo(base, altura))
        if opcion == 4:
            print("Hasta luego!")
            break
menu()