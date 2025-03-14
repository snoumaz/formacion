"""
EJERCICIO 2 : ÁREA DE UN TRIÁNGULO
Haz un programa que pida al usuario dos números, 
indicando que son la base y la altura de un triángulo
La respuesta del programa será:
"El área de un triángulo de base X y altura Y es Z" (los valores que sean)
"""

base = float(input("Introduce el valor de la Base: "))
altura = float(input("Introduce el valor de la Altura: "))

area = (0.5 * base * altura)
print(f"El área de un triángulo de base {base} y altura {altura} es {area}")