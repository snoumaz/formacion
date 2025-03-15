"""
EJERCICIO 3 : INTERCAMBIO DE VALORES
Haz un programa que pida al usuario dos valores (de cualquier tipo), 
por ejemplo así:
"Escribe el valor de la primera variable (a) --> "
Supongamos que responde X; lo guardas en la variable a
"Escribe el valor de la segunda variable (b) --> "
Supongamos que responde Y; lo guardas en la variable b
A continuación debes hacer que b tenga el valor de a y a el de b,
es decir, deben intercambiar sus valores
La respuesta del programa será:
"Ahora a vale Y y b vale X" (los valores que sean)
"""

valor1 = input("Escribe el valor de la primera variable (a) --> ")
valor2 = input("Escribe el valor de la segunda variable (b) --> ")

# Intercambiar los valores
valor1, valor2 = valor2, valor1

print(f"Ahora a vale {valor1} y b vale {valor2}")