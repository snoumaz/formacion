"""
Crea una clase “Persona”. Con atributos nombre y edad. Además, hay que crear un método “cumpleaños”,
que aumente en 1 la edad de la persona cuando se invoque sobre un objeto creado con “Persona”.
"""
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
    def cumpleaños(self):
        self.edad += 1
        print(f"{self.nombre} tiene {self.edad} años.")
        
# Crear un objeto de la clase Persona
persona1 = Persona("Juan", 25)
# Invocar el método cumpleaños
persona1.cumpleaños()




