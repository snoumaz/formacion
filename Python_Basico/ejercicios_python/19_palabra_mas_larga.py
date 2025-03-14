"""
De un texto encuentra las pabras mas largas y imprime en pantalla
"""

texto = input("Introduce un texto: ").lower().strip().split() # Esta variable tranforma en lista,un texto poniendo todas en minusculas y quitando los espacios 
#print(texto) # Muestra de control
larga = max(len(palabra) for palabra in texto) # la variable larga busca la palabra mas larga en el texto y la guarda en una lista
print(larga) # Muestra de control
for palabra in texto: # para cada palabra en el texto ejecuta el codigo
    if len(palabra) == larga: # si la palabra tiene el mismo numero de letras que larga muestra en pantalla
        print(palabra)

