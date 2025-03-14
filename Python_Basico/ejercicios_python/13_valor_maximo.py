'''
EJERCICIO 13: VALOR MÁXIMO
En una sola instrucción (de una vez) pide al usuario
que introduzca varios números.
La respuesta del programa será el valor máximo de todos ellos

Por ejemplo, si escribe
2, 5, 3
La respuesta debe ser:
"El valor máximo es 5" 
'''
try:
    print("El valor máximo es", max([int(x) for x in input("Introduce varios números separados por comas: ").split(",")]))
except:
    print("Error, introduce solo números separados por comas")