num1 = 0
num2 = 0
num3 = 0
resp = "S"

while resp == "S" or resp == "s":
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    num3 = int(input("Ingrese el tercer número: "))

    if (num1 >= num2) and (num1 >= num3):
        print("El numero mayor es: " ,num1)
    elif (num2 >= num1) and (num2 >= num3):
        print("El numero mayor es: ",num2)
    elif (num3 >= num2) and (num3 >= num1):
        print("El numero mayor es: ",num3)
    
    resp = str(input("¿Quieres repetir otra vez? (S/N) : "))
