"""
Ejercicio 1
Realizar un programa que conste de una clase llamada Estudiante, que tenga como atributos el nombre y la nota del alumno.
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""
class Estudiante(): # Crea una clase estudiante
    def __init__(self,nombre,nota): # crea el consutructor y le da atributos
        self.nombre = nombre # asigna el nombre del estudiante al atributo nombre
        self.nota = nota # asigna la nota del estudiante al atributo nota

    def imprimir(self): # crea un metodo para imprimir los datos del estudiante
        print("Nombre del estudiante: ",self.nombre) # imprime el nombre del estudiante
        print("Nota del estudiante: ",self.nota) # imprime la nota del estudiante

        if self.nota >= 5: # condicional para determinar si la nota es mayor o igual a 5
            print("El estudiante ha aprobado") # imprime que el estudiante ha aprobado
        else: # si la nota es menor a 5
            print("El estudiante no ha aprobado") # imprime que el estudiante no ha aprobado

            
estudiante1 = Estudiante("Juan",7)
estudiante2 = Estudiante("Ana",4)
estudiante1.imprimir() # crea dos objetos de la clase Estudiante y los imprime con sus respectivas notas y estados.
estudiante2.imprimir() # crea dos objetos de la clase Estudiante y los imprime con sus respectivas notas y estados.
