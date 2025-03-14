'''
EJERCICIO 11: SUMA CONSECUTIVA
Haz un programa que pida al usuario un número comprendido entre 1 y 10
y muestre la suma de todos los números anteriores 
empezando por el 1 y acabando en el propio número del usuario.

Por ejemplo, si escribe 3, 
la operación debe ser 1 + 2 + 3 = 6
Si escribe 5,
la operación debe ser 1 + 2 + 3 + 4 + 5 = 15

'''

try:
    numero = int(input("Introduce un número entre 1 y 10: \n"))
    suma = 0
    if numero < 1 or numero > 10:
        print("El número ha de estar entre 1 y 10")
        exit()
    for i in range(1, numero + 1):
        suma += i
    print(f"La suma de los números del 1 al {numero} es {suma}")
except ValueError:
    print("Ha de ser numerico")