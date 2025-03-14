"""
Para estructurar el código de un proyecto en Python esta es una manera de hacerlo:
"""

# Importa las librerías necesarias
import os
import sys

# Crear las variables globales
nombre = "Anna"
apellido = "Garcia"
edad = 20

# Crear las funciones necesarias para el proyecto

def mostrar_datos_alumno(nombre, apellido, becado=False):
    """
    Esta función muestra los datos del alumno y si tiene beca.
    """
    becado = "Sí" if becado else "No"
    return f"¿El alumno {nombre} {apellido} tiene beca? --> {becado}"

def sumar(*argv):
    """
    Esta función imprime el tipo de los argumentos recibidos.
    """
    print(type(argv))

# Crear el código principal del proyecto

def main():
    print("Esto es el código principal")
    print(f"El nombre del alumno es {nombre} {apellido} y tiene {edad} años")
    alumno_1 = mostrar_datos_alumno("Anna", "Garcia")
    print(alumno_1)
    alumno_2 = mostrar_datos_alumno("Joan", "Pou", True)
    print(alumno_2)
    sumar(1, 2)
    print("Fin del código principal")

# Crear el código de pruebas

def test_mostrar_datos_alumno():
    print("Esto es el código de pruebas")
    assert mostrar_datos_alumno("Anna", "Garcia") == "¿El alumno Anna Garcia tiene beca? --> No"
    assert mostrar_datos_alumno("Joan", "Pou", True) == "¿El alumno Joan Pou tiene beca? --> Sí"

# Crear el código de documentación

def documentacion():
    print("Esto es el código de documentación")
    print("Documentación de la función mostrar_datos_alumno")
    print(mostrar_datos_alumno.__doc__)
    print("Documentación de la función sumar")
    print(sumar.__doc__)
    print("Documentación de la función documentacion")
    print(documentacion.__doc__)

# Crear el código de ejecución de la aplicación

if __name__ == "__main__":
    print("Inicio de la aplicación")
    main()
    test_mostrar_datos_alumno()
    documentacion()
    print("Fin de la aplicación")

# fin del código
# Nota: el código de documentación y de pruebas no es necesario en todos los proyectos, pero es recomendable hacerlo para tener un código más limpio y ordenado