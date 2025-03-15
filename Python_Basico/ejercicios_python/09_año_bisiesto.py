'''
EJERCICIO 9: AÑO BISIESTO
Haz un programa que pida al usuario un año y diga si es bisiesto o no
Averigua cual es el criterio
'''

try:
    año = int(input("Introduce un año: \n"))
    if año % 4 == 0 and año % 100 != 0 or año % 400 == 0: # Averiguar si el año es bisiesto
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")
except ValueError:
    print("Ha de ser numerico")