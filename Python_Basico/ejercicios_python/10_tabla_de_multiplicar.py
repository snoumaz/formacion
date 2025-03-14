'''
EJERCICIO 10: TABLA DE MULTIPLICAR
Haz un programa que pida al usuario un número 
y muestre la tabla de multiplicar de ese número
desde 1 hasta 10, ambos incluidos
'''

try:
    numero = int(input("Introduce un número: \n"))
    for tabla in range(1, 11):
        print(f"{numero} x {tabla} = {numero * tabla}")
except ValueError:
    print("Ha de ser numerico")