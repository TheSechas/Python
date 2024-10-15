
multiplos = list()

n = int(input("Introduce el valor de n: "))

if n % 5 == 0:
    for i in range(5, n + 1, 5):
        multiplos.append(i)
else: 
    for i in range(5, n, 5):
        multiplos.append(i)

print(f"Los multipos de 5 son: {multiplos}")