'''
EJERCICIO 7: POSITIVO, NEGATIVO O CERO
Haz un programa que pida al usuario un número y diga si es positivo, 
negativo o cero
'''
try:
    numero = float(input("Introduce un número: \n"))
    if numero > 0:
        print("El número es positivo")
    elif numero < 0:
        print("El número es negativo")
    else:
        print("El número es cero")
except ValueError:
    print("Ha de ser numerico")