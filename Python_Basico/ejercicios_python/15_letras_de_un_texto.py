'''
EJERCICIO 15: LETRAS DE UN TEXTO
Haz un programa que pida al usuario un texto.
El programa debe mostrar las letras que aparecen en ese texto
ordenadas de forma alfabética, pero solo una vez por cada letra,
y siempre en minúsculas.

Por ejemplo, si escribe: "Hoy es domingo"
La respuesta debe ser: "deghimny"
'''

try:
    print("".join(sorted(set([x for x in input("Introduce un texto: ").lower() if x.isalpha()]))))
except:
    print("Error, introduce un texto válido")