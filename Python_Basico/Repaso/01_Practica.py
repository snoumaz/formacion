"""
Practica 01: Compara dos variables
Descripcion: Este programa compara dos variables y determina si son iguales o diferentes.
Para ello debes crear una clase Persona con los atributos nombre y edad, luego crea un objeto de esta clase 
y asignale valores a sus atributos. 
Finalmente, compara estos objetos para ver si son iguales o no.
Deberas usar una funcion de comparacion.
"""
class Persona(): # Clase Persona con dos atributos, nombre y edad.
    def __init__(self,nombre,edad): # Constructor de la clase Persona.
        self.nombre = nombre # Atributo nombre.
        self.edad = edad # Atributo edad.

p1 = Persona("Juan", 25) # Creacion de un objeto de la clase Persona con el nombre "Juan" y la edad 25.
p2 = Persona("Pedro", 25) # Creacion de otro objeto de la clase Persona con el nombre "Pedro" y la edad 25.

#print(p1.nombre == p2.nombre and p1.edad == p2.edad) # Comparacion de los dos objetos. Si son iguales, imprime True, si no, False.

# Funcion para comparar dos objetos de la clase Persona.
def comparar_personas(persona1,persona2):
    if persona1.nombre == persona2.nombre and persona1.edad == persona2.edad:    
        return f"{persona1.nombre} y {persona2.nombre} son iguales. Ambos tienen {persona1.edad} años."
    elif persona1.nombre == persona2.nombre and persona1.edad != persona2.edad:
        return f"{persona1.nombre} y {persona2.nombre} son iguales en nombre, pero tienen diferentes edades. {persona1.nombre} tiene {persona1.edad} años y {persona2.nombre} tiene {persona2.edad} años."
    elif persona1.nombre != persona2.nombre and persona1.edad == persona2.edad:
        return f"{persona1.nombre} y {persona2.nombre} no son iguales, pero ambos tienen {persona1.edad} años."
    elif persona1.nombre != persona2.nombre and persona1.edad != persona2.edad:
        return f"{persona1.nombre} y {persona2.nombre} no son iguales ni en nombre ni en edad. {persona1.nombre} tiene {persona1.edad} años y {persona2.nombre} tiene {persona2.edad} años."
    else:
        return "Error: No se proporcionaron dos personas para comparar."
    
print(comparar_personas(p1, p2)) # Imprime el resultado de la comparación entre p1 y p2.



