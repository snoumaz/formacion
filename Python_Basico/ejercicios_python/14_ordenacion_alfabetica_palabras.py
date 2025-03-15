'''
EJERCICIO 14: ORDENACIÓN ALFABÉTICA DE PALABRAS
Haz un programa que pida al usuario un texto.
El programa debe ordenar las palabras del texto de forma alfabética.

Por ejemplo, si escribe: "hoy es domingo"
La respuesta debe ser: "domingo es hoy"
'''
try:
    print(" ".join(sorted(input("Introduce un texto: ").split(" "))))
except:
    print("Error, introduce un texto válido")