'''
EJERCICIO 16: NÚMEROS AL CUADRADO
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar el cuadrado de cada uno de los números.

Por ejemplo, si escribe:
2, 5, 3
La respuesta debe ser:
4, 25, 9
'''
try:
    print(", ".join([str(float(x)**2) for x in input("Introduce varios números separados por coma: ").split(",")]))
except:
    print("Error, introduce solo números separados por coma")
