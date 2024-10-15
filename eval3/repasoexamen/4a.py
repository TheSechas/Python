# Define una lista de letras válidas para las matrículas de automóviles
letras_validas = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

# Define una función para obtener la matrícula del usuario
def get_matricula():
    # Solicita al usuario que ingrese los 4 números de la matrícula
    num_matricula = input("Escribe los 4 números de tu matrícula: ")
    # Verifica si la longitud de la entrada es correcta y si todos los caracteres son dígitos
    if len(num_matricula) != 4 or not num_matricula.isdigit() or int(num_matricula) > 9999:
        print("Tu matrícula no es válida.")
        return None, None  # Si la matrícula no es válida, devuelve None para ambos valores
    # Solicita al usuario que ingrese las 3 letras de la matrícula y las convierte a mayúsculas
    let_matricula = input("Escribe las 3 letras de tu matrícula: ").upper()
    # Verifica si la longitud de las letras es correcta y si todas son letras válidas
    if len(let_matricula) != 3 or any(letra not in letras_validas for letra in let_matricula):
        print("Tu matrícula no es válida.")
        return None, None  # Si las letras no son válidas, devuelve None para ambos valores
    return int(num_matricula), let_matricula  # Devuelve los números y las letras de la matrícula

# Define una función para incrementar las letras de la matrícula
def incrementar_letras(letras):
    letras = list(letras)  # Convierte las letras en una lista para poder modificarlas
    carry = True  # Variable para controlar el acarreo al incrementar las letras
    # Itera sobre las letras en orden inverso (de derecha a izquierda)
    for i in range(2, -1, -1):
        if carry:
            idx = letras_validas.index(letras[i])  # Obtiene el índice de la letra en la lista de letras válidas
            if idx == len(letras_validas) - 1:  # Si la letra es la última en la lista de letras válidas
                letras[i] = letras_validas[0]  # Reinicia la letra a la primera letra válida
                carry = True  # Habilita el acarreo para la siguiente letra
            else:
                letras[i] = letras_validas[idx + 1]  # Incrementa la letra a la siguiente letra válida
                carry = False  # Deshabilita el acarreo
        else:
            break  # Sale del bucle si no hay acarreo
    return ''.join(letras)  # Convierte las letras de nuevo a una cadena y la devuelve

# Define una función para generar la siguiente matrícula
def siguiente_matricula():
    num_matricula, let_matricula = get_matricula()  # Obtiene los números y las letras de la matrícula del usuario
    if num_matricula is None or let_matricula is None:
        return  # Si la matrícula no es válida, termina la función
    if num_matricula == 9999:  # Si el número de la matrícula es 9999
        num_matricula = 0  # Reinicia el número a 0000
        let_matricula = incrementar_letras(let_matricula)  # Incrementa las letras de la matrícula
    else:
        num_matricula += 1  # Incrementa el número de la matrícula en 1
    # Imprime la siguiente matrícula formateada con ceros a la izquierda para el número
    print(f"{num_matricula:04d} {let_matricula}")

# Llama a la función para generar la siguiente matrícula
siguiente_matricula()
