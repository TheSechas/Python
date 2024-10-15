# Lista de letras válidas excluyendo vocales y Ñ
letras_validas = "BCDFGHJKLMNPQRSTVWXYZ"

def incrementar_letras(letras):
    # Convierte la cadena de letras en una lista para modificar individualmente
    letras = list(letras)
    carry = True
    # Itera sobre las letras desde la última a la primera
    for i in range(2, -1, -1):
        if carry:
            idx = letras_validas.index(letras[i])
            if idx == len(letras_validas) - 1:
                # Si la letra actual es la última en letras_validas, la cambia a la primera letra
                letras[i] = letras_validas[0]
                carry = True  # Continúa el carry a la siguiente posición
            else:
                # Si no es la última, incrementa a la siguiente letra y para el carry
                letras[i] = letras_validas[idx + 1]
                carry = False
        else:
            break
    return ''.join(letras)

def siguiente_matricula(numero, letras):
    # Incrementa el número
    if numero == 9999:
        numero = 0
        letras = incrementar_letras(letras)
    else:
        numero += 1
    return f"{numero:04d} {letras}"

# Solicita la matrícula al usuario
entrada = input("Introduce la matrícula (ej. 1234 BBB): ")
numero, letras = entrada.split()

numero = int(numero)  # Convierte el número a entero
letras = letras.upper()  # Asegura que las letras estén en mayúsculas

# Obtiene la siguiente matrícula
nueva_matricula = siguiente_matricula(numero, letras)

# Muestra la nueva matrícula
print(f"La siguiente matrícula es: {nueva_matricula}")
