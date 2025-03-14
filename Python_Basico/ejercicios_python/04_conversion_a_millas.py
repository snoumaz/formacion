"""
EJERCICIO 4 : CONVERSIÓN A MILLAS
Haz un programa que pida al usuario la distancia a convertir (en km)
Redondea el resultado a dos decimales
La respuesta del programa será:
"X km equivalen a Y millas" (los valores que sean)
Nota: 1 km son 0.621371 millas
"""


milla = 0.621371
try:
    distancia = float(input("Introduce una distancia en KM: \n"))
    resultado = distancia * milla
    print(f"{distancia} km equivalen a {resultado} millas")
except ValueError:
    print("Ha de ser numerico")