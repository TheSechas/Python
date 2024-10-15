lista1 = list()

def solicitar_lista():
    fin = 0
    numero = 0
    lista = list()
    print(f"Introduce números hasta teclear un carácter no numérico.")
    while fin == 0:
        try:
            numero = int(input("Introduce número:"))
            lista.append(numero)
        except ValueError:
            fin = 1
    return(lista)

def calcula_moda(lista):
    cont = 0
    frecu = 0

    for cont in lista:
        if frecu < lista.count(cont):
            frecu = lista.count(cont)
            moda = cont
    return(moda)

lista1 = solicitar_lista()
print(f"La moda de lista1 es: {calcula_moda(lista1)}")
