"""
Solicita al usuario un numero y haz la tabla de multiplicar 
"""
import os
os.system("cls")
try: # Prueba y captura de errores
    numero = int(input("Introduce un numero del 1 al 10 \n")) # Introduce un numero del 1 al 10
    if 0<= numero <= 10: # Compara si el numero es mayor que 0 y menor de 10
        for num in range(11): # Recorre la lista de numeros del 0 al 10
            print(f"{numero} * {num} = {numero*num}") # Imprime la tabla de multiplicar del numero introducido por el usuario por el numero de la lista de 0 al 10
    else:
        print("Solo numeros del 1 al 10") # Si el numero es menor de 0 o mayor de 10 imprime mensaje
except ValueError:
    print("Solo son validos numeros") # Si el usuario introduce un valor no valido imprime mensaje

try:
    numero = int(input("Introduce un numero del 1 al 10 \n")) # Introduce un numero del 1 al 10
    for num in range(11): # Recorre la lista de numeros del 0 al 10
        print(f"{numero} * {num} = {numero*num}") # Imprime la tabla de multiplicar del numero introducido por el usuario por el numero de la lista de 0 al 10
except ValueError:
    print("Solo son validos numeros") # Si el usuario introduce un valor no valido imprime mensaje