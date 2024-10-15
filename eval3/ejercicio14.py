lista1 = [1,2,2,3,3,3,4,4,4,4,5,20]
lista2 = [1,8,9,6,3,2,1,5,4,7,9,6,3,2,1,4,7]

def calcula_moda(lista):
    cont = 0
    frecu = 0

    for cont in lista:
        if frecu < lista.count(cont):
            frecu = lista.count(cont)
            moda = cont
    return(moda)

print(f"La moda de lista1 es: {calcula_moda(lista1)}")
print(f"La moda de lista2 es: {calcula_moda(lista2)}")