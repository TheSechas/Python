num = [0] * 10

for i in range(10):
    num[i] = int(input("Introduce un número entero: "))

print("los números del array son: ")

num.sort(reverse=True)
for num in num:
    print(num)
