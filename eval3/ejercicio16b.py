def incrementar_letra(letra):
    letras_validas = "BCDFGHJKLMNPQRSTVWXYZ"
    indice = letras_validas.index(letra)
    if indice == len(letras_validas) - 1:
        return 'B', True  # Si es 'Z', vuelve a 'B' y hay acarreo
    else:
        return letras_validas[indice + 1], False

def siguiente_matricula(matricula):
    numero, letras = matricula.split()
    numero = int(numero)
    
    # Incrementar los números
    if numero < 9999:
        numero += 1
        return f"{numero:04d} {letras}"
    
    # Si el número es 9999, reiniciar a 0000 y manejar el acarreo a las letras
    numero = 0
    letras = list(letras)
    
    # Incrementar las letras de derecha a izquierda
    carry = True
    for i in range(2, -1, -1):
        if carry:
            letras[i], carry = incrementar_letra(letras[i])
        else:
            break
    
    return f"{numero:04d} {''.join(letras)}"

# Casos de prueba
casos_de_prueba = ["1234 BBB", "9999 BBZ", "9999 BBD", "9999 ZZZ"]

for caso in casos_de_prueba:
    print(siguiente_matricula(caso))
