
# Visualizar los múlƟplos de 4 comprendidos entre 4 y N, donde N es introducido por pantalla.

num = 0
i = 0

num = int(input("Introduce un numero: "))
print(f"Los numeros multiplos de 4 entre 4 y {num} son: ")
for i in range(4, num+1):
    if i % 4 == 0:
        print(i)






