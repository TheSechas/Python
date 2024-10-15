def  Celsius_a_Fahrenheit(celsius):
    return celsius * 9/5 + 32

def Celsius_a_Kelvin(celsius):
    return celsius + 273.15

def Fahrenheit_a_Celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def Fahrenheit_a_Kelvin(fahrenheit):
    return ((fahrenheit - 32) * 5/9)

def Kelvin_a_Celsius(kelvin):
    return kelvin - 273.15

def Kelvin_a_Fahrenheit(kelvin):
    return (kelvin - 273.15)

def menu():
    while True:
        print("1.- Convertir de Celsius a Fahrenheit")
        print("2.- Convertir de Celsius a Kelvin")
        print("3.- Convertir de Fahrenheit a Celsius")
        print("4.- Convertir de Fahrenheit a Kelvin")
        print("5.- Convertir de Kelvin a Celsius")
        print("6.- Convertir de Kelvin a Fahrenheit")
        print("7.- Salir.")

        opcion = int(input("Selecione lo que desee convertir: "))
        
        if opcion == 1:
            celsius = float(input("Indique los grados Celsius: "))
            print("Son", Celsius_a_Fahrenheit(celsius), "grados Fahrenheit")
        if opcion == 2:
            celsius = float(input("Indique los grados Celsius: "))
            print("Son", Celsius_a_Kelvin(celsius), "grados Kelvin")
        if opcion == 3:
            fahrenheit = float(input("Indique los grados Fahrenheit: "))
            print("Son", Fahrenheit_a_Celsius(fahrenheit), "grados Celsius")
        if opcion == 4:
            fahrenheit = float(input("Indique los grados Fahrenheit: "))
            print("Son", Fahrenheit_a_Kelvin(fahrenheit), "grados Kelvin")
        if opcion == 5:
            kelvin = float(input("Indique los grados Kelvin: "))
            print("Son", Kelvin_a_Celsius(kelvin), "grados Celsius")
        if opcion == 6:
            kelvin = float(input("Indique los grados Kelvin: "))
            print("Son", Kelvin_a_Fahrenheit(kelvin), "grados Fahrenheit")
        if opcion == 7:
            print("Hasta luego!")
            break
menu()