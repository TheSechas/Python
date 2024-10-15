letras_validas = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

def get_matricula():
    num_matricula = input("Escribe los 4 números de tu matrícula: ")
    if len(num_matricula) != 4 or not num_matricula.isdigit() or int(num_matricula) > 9999:
        print("Tu matrícula no es válida.")
        return None, None
    let_matricula = input("Escribe las 3 letras de tu matrícula: ").upper()
    if len(let_matricula) != 3 or any(letra not in letras_validas for letra in let_matricula):
        print("Tu matrícula no es válida.")
        return None, None
    return int(num_matricula), let_matricula

def incrementar_letras(letras):
    letras = list(letras)
    carry = True
    for i in range(2, -1, -1):
        if carry:
            idx = letras_validas.index(letras[i])
            if idx == len(letras_validas) - 1:
                letras[i] = letras_validas[0]
                carry = True
            else:
                letras[i] = letras_validas[idx + 1]
                carry = False
        else:
            break
    return ''.join(letras)

def siguiente_matricula():
    num_matricula, let_matricula = get_matricula()
    if num_matricula is None or let_matricula is None:
        return

    if num_matricula == 9999:
        num_matricula = 0
        let_matricula = incrementar_letras(let_matricula)
    else:
        num_matricula += 1

    print(f"{num_matricula:04d} {let_matricula}")

siguiente_matricula()
