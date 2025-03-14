"""
Tenemos esta lista de animales

Vamos a pedir una letra al usuario
Mostraremos los animales que continen esa letra
Y si no hay ninguno diremos "Ningun animal contiene esa letra"
"""
import os
os.system("cls")
animales = ["gato", "perro", "caballo", "paloma", "murcielago","leon", "mono"]
letra = input("Introduce una letra: \n").lower()

if len(letra) != 1 or not letra.isalpha(): # Validamos que la letra sea un solo carácter y no esté vacía
    print("Ha de ser una sola letra del abecedario") # Muestra un mensaje de error si no cumple la condición
else:
    encontrado = False #  Encontrado
    for animal in animales: # Recorremos la lista de animales
        if letra in animal.lower(): # Si la letra está en el animal en minúsculas
            print(animal) # Muestra el animal que contiene la letra
            encontrado = True # Marca que se ha encontrado un animal que contiene la letra
    if not encontrado: # Si no se ha encontrado ningún animal que contenga la letra
        print("Ningun animal contiene esa letra")



    