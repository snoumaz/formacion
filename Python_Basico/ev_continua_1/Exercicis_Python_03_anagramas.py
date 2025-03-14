"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 3
Un anagrama es un texto o palabra resultante de modificar el orden de otro texto o palabra.
Los textos deberán ir sin tildes (acentos o diéresis)
No se tienen en cuenta mayúsculas ni espacios.

Mostraremos el mensaje: "Anagramas"
Pediremos al usuario un texto/palabra.
Pediremos al usuario un segundo texto/palabra
Responderemos si ambos son anagramas o no.

Por ejemplo:
    "Introduzca el primer texto --> " Pedro
    "Introduzca el segundo texto --> " Poder
    "Son anagramas --> Sí"

Otro ejemplo:
    "Introduzca el primer texto --> " Ramon
    "Introduzca el segundo texto --> " Morir
    "Son anagramas --> No"
 
"""
print("Anagramas")

# Pedir los textos al usuario
texto1 = input("Introduzca el primer texto --> ").lower()                           # Convertir a minúsculas
texto2 = input("Introduzca el segundo texto --> ").lower()                          # Convertir a minúsculas  

# Eliminar tildes manualmente y caracteres no alfabéticos
texto1_limpio = ""                                                                  # Variable que almacenará el texto limpio       
for caracter in texto1:                                                             # Recorrer cada caracter del texto
    if caracter == 'á':                                                             # Si el caracter es una 'á' lo sustituye por 'a'
        texto1_limpio += 'a'                                                        # Añade 'a' al texto limpio
    elif caracter == 'é':                                                           # Si el caracter es una 'é' lo sustituye por 'e'     
        texto1_limpio += 'e'                                                        # Añade 'e' al texto limpio                         
    elif caracter == 'í':                                                           # Si el caracter es una 'í' lo sustituye por 'i'                           
        texto1_limpio += 'i'                                                        # Añade 'i' al texto limpio
    elif caracter == 'ó':                                                           # Si el caracter es una 'ó' lo sustituye por 'o'   
        texto1_limpio += 'o'                                                        # Añade 'o' al texto limpio
    elif caracter == 'ú' or caracter == 'ü':                                        # Si el caracter es una 'ú' o 'ü' lo sustituye por 'u'
        texto1_limpio += 'u'                                                        # Añade 'u' al texto limpio             
    elif 'a' <= caracter <= 'z':                                                    # Si el caracter es una letra añade el caracter al texto limpio
        texto1_limpio += caracter                                                   # Añade el caracter al texto limpio    

texto2_limpio = ""                                                                  # Variable que almacenará el texto limpio
for caracter in texto2:                                                             # Recorrer cada caracter del texto
    if caracter == 'á':                                                             # Si el caracter es una 'á' lo sustituye por 'a'
        texto2_limpio += 'a'                                                        # Añade 'a' al texto limpio             
    elif caracter == 'é':                                                           # Si el caracter es una 'é' lo sustituye por 'e'                               
        texto2_limpio += 'e'                                                        # Añade 'e' al texto limpio
    elif caracter == 'í':                                                           # Si el caracter es una 'í' lo sustituye por 'i'
        texto2_limpio += 'i'                                                        # Añade 'i' al texto limpio
    elif caracter == 'ó':                                                           # Si el caracter es una 'ó' lo sustituye por 'o'           
        texto2_limpio += 'o'                                                        # Añade 'o' al texto limpio 
    elif caracter == 'ú' or caracter == 'ü':                                        # Si el caracter es una 'ú' o 'ü' lo sustituye por 'u'
        texto2_limpio += 'u'                                                        # Añade 'u' al texto limpio
    elif 'a' <= caracter <= 'z':                                                    # Si el caracter es una letra añade el caracter al texto limpio     
        texto2_limpio += caracter                                                   # Añade el caracter al texto limpio         

# Verificar si tienen la misma longitud
if len(texto1_limpio) != len(texto2_limpio):                                        # Si la longitud de los textos limpios es diferente             
    print("Son anagramas --> No")
else:
    # Convertir a listas
    lista_texto1 = list(texto1_limpio)                                              # Convertir el texto limpio en una lista              
    lista_texto2 = list(texto2_limpio)                                              # Convertir el texto limpio en una lista          

    
    indice_actual = 0                                                               # Variable que almacenará el índice actual
    while indice_actual < len(lista_texto1):                                        # Mientras el índice actual sea menor que la longitud de la lista_texto1        
        indice_comparacion = indice_actual + 1                                      # Variable que almacenará el índice de comparación
        while indice_comparacion < len(lista_texto1):                               # Mientras el índice de comparación sea menor que la longitud de la lista_texto1
            if lista_texto1[indice_actual] > lista_texto1[indice_comparacion]:      # Si el elemento actual es mayor que el elemento de comparación
                temp = lista_texto1[indice_actual]                                  # Intercambia los elementos
                lista_texto1[indice_actual] = lista_texto1[indice_comparacion]      # Intercambia los elementos
                lista_texto1[indice_comparacion] = temp                             # Intercambia los elementos mete el valor de la variable temp en la posición de la lista_texto1[indice_comparacion] que se ha guardado en la variable temp
            if lista_texto2[indice_actual] > lista_texto2[indice_comparacion]:      # Si el elemento actual es mayor que el elemento de comparación
                temp = lista_texto2[indice_actual]                                  # Intercambia los elementos               
                lista_texto2[indice_actual] = lista_texto2[indice_comparacion]      # Intercambia los elementos
                lista_texto2[indice_comparacion] = temp                             # Intercambia los elementos mete el valor de la variable temp en la posición de la lista_texto2[indice_comparacion] que se ha guardado en la variable temp   
            indice_comparacion += 1                                                 # Incrementa el índice de comparación
        indice_actual += 1                                                          # Incrementa el índice actual             

    # Comparar listas ordenadas
    if lista_texto1 == lista_texto2:                                                # Si las listas son iguales
        print("Si son anagramas")
    else:
        print("No son anagramas")                                                   # Si las listas no son iguales
