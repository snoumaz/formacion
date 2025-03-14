"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 2a

Mostraremos el texto: "Contar letras en un texto"

Pediremos al usuario un texto, así:
"Por favor, introduzca un texto "
Puede contener números y caracteres con tilde.

A continuación mostraremos las letras que contiene y cuantas son,
ordenadas por número de apariciones. En caso de empate, en orden alfabético. 
Ignoraremos los números, los espacios y los signos de puntuación 
(punto, coma, punto y coma, exclamación, etc.)
Consideremos mayúsculas y minúsculas como la misma letra.

Por ejemplo:
"Por favor, introduzca un texto " ¿Amar?
La respuesta sería: 
"El texto contiene las letras:
a, 2 veces
m, 1 vez
r, 1 vez
"

Por ejemplo:
"Por favor, introduzca un texto " Python forever and ever
La respuesta sería: 
"El texto contiene las letras:
e, 4 veces
r, 3 veces
o, 2 veces
n, 2 veces
a, 1 vez
f, 1 vez
h, 1 vez
p, 1 vez
v, 1 vez
y, 1 vez
"

# Ejercicio 2b

# Mostraremos el texto: "Contar palabras en un texto"
# Lo mismo que el ejercicio anterior, pero con palabras en lugar de letras.
# . 
"""
print("Contar letras en un texto") # Mostrar el título	

# Pedir al usuario que introduzca un texto
texto = input("Por favor, introduzca un texto: ").lower()                           # esta línea toma el texto introducido por el usuario y lo pasa a minúsculas

# Filtrar solo letras y contar ocurrencias manualmente
letras = {}                                                                         # Diccionario que almacenará las letras y su cantidad de ocurrencias
for c in texto:                                                                     # Recorrer cada caracter del texto
    if c.isalpha():                                                                 # Si el caracter es una letra añade la letra al diccionario, si ya está añade 1
        if c in letras:                                                             # Si la letra ya está en el diccionario añade 1
            letras[c] += 1 
        else:                                                                       # Si la letra no está en el diccionario añade la letra con una cantidad de 1
            letras[c] = 1

# Ordenar manualmente: primero por cantidad descendente, luego alfabéticamente
letras_ordenadas = []                                                               # Lista que almacenará las letras ordenadas
for letra, cantidad in letras.items():                                              # Para cada letra y su cantidad en el diccionario añade la letra y su cantidad a la lista letras_ordenadas
    insertado = False                                                               # Variable para saber si se ha insertado la letra en la lista
    for i in range(len(letras_ordenadas)):                                          # Recorrer la lista letras_ordenadas
        if cantidad > letras_ordenadas[i][1]:                                       # Orden descendente por cantidad
            letras_ordenadas.insert(i, (letra, cantidad))                           # Orden descendente por cantidad
            insertado = True                                                        # si se ha insertado la letra en la lista
            break
        elif cantidad == letras_ordenadas[i][1] and letra < letras_ordenadas[i][0]: # si hay empate, ordenamos alfabéticamente
            # Si hay empate, ordenamos alfabéticamente
            letras_ordenadas.insert(i, (letra, cantidad))                           # la variable letras_ordenadas insertado en la posición correcta
            insertado = True                                                        # si se ha insertado la letra en la lista
            break
    if not insertado:                                                               # Si no se ha insertado la letra en la lista
        letras_ordenadas.append((letra, cantidad))                                  # añade la letra y su cantidad a la lista letras_ordenadas

# Mostrar las letras y su cantidad de ocurrencias ordenadas
if letras_ordenadas:                                                                # Si hay letras en el texto
    print("El texto contiene las letras:")
    for letra, cantidad in letras_ordenadas:                                        # Para cada letra y su cantidad en la lista letras_ordenadas                            
        if cantidad == 1:                                                           # Si la cantidad de la letra es 1              
            print(letra + ", " + str(cantidad) + " vez")                            # Muestra la letra y su cantidad de ocurrencias
        else:
            print(letra + ", " + str(cantidad) + " veces")                          # Muestra la letra y su cantidad de ocurrencias
else:
    print("No se encontraron letras en el texto.")
