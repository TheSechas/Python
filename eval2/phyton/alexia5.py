numenor = int(input("Introduce el límite inferior del intervalo: "))
numayor = int(input("Introduce el límite superior del intervalo: "))

if numenor > numenor:
    numenor, numayor = numayor, numenor

print(f"Números impares en el intervalo [{numenor}, {numayor}]:")
for num in range(numenor, numayor + 1):
    if num % 2 != 0:
        print(num)
