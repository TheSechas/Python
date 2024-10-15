def siguiente_matricula(matricula):
    letras_validas = "BCDFGHJKLMNPQRSTVWXYZ"
    numero, letras = matricula[:4], matricula[5:]
    
    # Incrementar los números
    nuevo_numero = int(numero) + 1
    if nuevo_numero > 9999:
        nuevo_numero = 0
        incrementar_letras = True
    else:
        incrementar_letras = False
    
    nuevo_numero = f"{nuevo_numero:04d}"
    
    # Incrementar las letras si es necesario
    if incrementar_letras:
        lista_letras = list(letras)
        for i in range(2, -1, -1):
            if lista_letras[i] == 'Z':
                lista_letras[i] = 'B'
            else:
                lista_letras[i] = letras_validas[letras_validas.index(lista_letras[i]) + 1]
                break
        else:
            # Caso especial donde todas las letras son Z y pasan a BBB
            lista_letras = ['B', 'B', 'B']
        nuevas_letras = "".join(lista_letras)
    else:
        nuevas_letras = letras
    
    return f"{nuevo_numero} {nuevas_letras}"

# Casos de prueba
casos_de_prueba = ["1235 BZZ", "9999 FZZ", "9929 ZDD", "0999 XXZ"]

for caso in casos_de_prueba:
    print(siguiente_matricula(caso))


