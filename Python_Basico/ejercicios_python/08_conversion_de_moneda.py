'''
EJERCICIO 8: CONVERSIÓN DE MONEDAS
Haz un programa que pida al usuario la cantidad de euros que quiere convertir a dólares
La respuesta del programa será:
"X euros equivalen a Y dólares" (los valores que sean)
Formúla de conversión : 1 euro = 1.18 dólares
'''

dolar = 1.18 
try:
    conversion = float(input("Introduce una cantidad Euros: \n"))
    resultado = conversion * dolar
    print(f"{conversion} euros equivalen a {resultado} dólares")
except ValueError:
    print("Ha de ser numerico")