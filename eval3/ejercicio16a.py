letras_validas = "BCDFGHJKLMNPQRSTVWXYZ"

def obtener_matricula():
    num_matricula = input("Ingresa los 4 números de tu matrícula: ")
    letras_matricula = input("Ingresa las 3 letras de tu matrícula: ").upper()

    if (not num_matricula.isdigit() or len(num_matricula) != 4 or int(num_matricula) >= 9999
            or len(letras_matricula) != 3 or any(letra not in letras_validas for letra in letras_matricula)):
        print("La matrícula no es válida.")
        return

    num_matricula = str(int(num_matricula) + 1).zfill(4)
    letras_matricula = incrementar_letras(letras_matricula)
    print(f"Matrícula siguiente: {num_matricula} {letras_matricula}")

def incrementar_letras(letras):
    letras = list(letras)
    for i in range(2, -1, -1):
        if letras[i] == 'Z':
            letras[i] = 'B'
        else:
            letras[i] = letras_validas[letras_validas.index(letras[i]) + 1]
            break
    return ''.join(letras)

obtener_matricula()
