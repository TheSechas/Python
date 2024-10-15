import random

def juego_adivinanza():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        intento = int(input("Adivina el número: "))
        intentos += 1

        if intento == numero_secreto:
            print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
            break
        elif intento < numero_secreto:
            print("El número es mayor. Intenta de nuevo.")
        else:
            print("El número es menor. Intenta de nuevo.")

if __name__ == "__main__":
    juego_adivinanza()