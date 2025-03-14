"""
Vamos a recibir un texto por parte del user.
Con ese texto vamos a generar otro sin las vocales ni los espacios.

"""

texto = input("Introduce un texto: \n").lower() # variable que el usuario introduce texto
for letras in "aeiou ": # para la variable letras en letras introduce "aeiou "
    palabras = texto.replace(letras,"") # introduce en la variable texto el reemplazo de la variable letras por espacios
print(palabras)


