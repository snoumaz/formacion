"""
EJERCICIO 5 : CONVERSIÓN A KM
Haz un programa que haga lo opuesto a lo anterior,
convertir millas es kilómetros
"""

km = 1.60934
try:
    distancia = float(input("Introduce una distancia en Millas: \n"))
    resultado = distancia * km
    print(f"{distancia} Millas equivalen a {resultado} KM")
except ValueError:
    print("Ha de ser numerico")