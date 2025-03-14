"""
El usuario introduce un número entero, como máximo 100
ese número es el límite
Desde 0 hasta el número introducido (los dos incluidos), vamos a listar todos los números
Pero...
-- Si el número es multiplo de 3, escribiremos 3 - FIZZ
-- Si el número es multiplo de 5, escribiremos 5 - BUZZ
-- Si el número es multiplo de 3 y de 5, escribiremos 3 - FIZZ-BUZZ
-- En los demás casos sólo el número
-- Si el usuario escribe más de 100 o menos de 0, diremos "El número es incorrecto"

"""
import os

try:
    numero = int(input("Introduce un numero del 1 al 100: \n")) 
    os.system("cls")
    print("Lista Numeros")
    if 0<numero<=100: # Compara si la variable numero es mayor que 0 y menor de 100
        for lista_numeros in range(numero + 1): # Recorre la lista de numeros
            if lista_numeros == 0: # Si el numero es 0 imprime 0
                print(0)
            elif lista_numeros % 3 == 0 and lista_numeros % 5 == 0: # Si el numero es multiplo de 3 y 5 imprime Fizz - Buzz
                print(f"{lista_numeros} - Fizz - Buzz")
            elif lista_numeros % 5 == 0: # Si el numero es multiplo de 5 imprime Buzz
                print(f"{lista_numeros} - Buzz")
            elif lista_numeros % 3 == 0: # Si el numero es multiplo de 3 imprime Fizz
                print(f"{lista_numeros} - Fizz")
            else:
                print(lista_numeros)
    else: # Si el numero es menos 0 o mas 100  imprime mensaje
        print("El número es incorrecto ")
    

except ValueError:
    print("El número es incorrecto ")

# Solucion Ferran

# try:
#     referencia = int(input("Introduce un numero del 1 al 100: \n"))
#     # if referencia < 0 or referencia > 100:
#     #     print("El numero es incorrecto")
#     #     exit()
#     if 0<= referencia <= 100: # Compara si la variable numero es mayor que 0 y menor de 100
#         for num in range(0, referencia+1, 1):
#             if num == 0:
#                 print(0)
#             elif num % 3 == 0 and num % 5 == 0:
#                 print(f"{num} -Fizz-Buzz")
#             elif num % 3 == 0:
#                 print(f"{num} -Fizz")
#             elif num % 5 == 0:
#                 print(f"{num} -Buzz")
#             else:
#                 print(num)
# except ValueError:
#     print("El numero es incorrecto")
