"""
Crear una clase llamada Marino(), con un método que sea hablar, en donde muestre un mensaje que diga «Hola, soy un animal marino!».
Luego, crear una clase Pulpo() que herede Marino, pero modificar el mensaje de hablar por «Hola soy un Pulpo!».
Por último, crear una clase Foca(), heredada de Marino, pero que tenga un atributo nuevo llamado mensaje y que muestre ese mesjae como parámetro.
"""

class Marino(): # Clase padre
    def hablar(self): # Método de la clase padre
        print("Hola, soy un animal marino!")
    
class Pulpo(Marino): # Clase hija que hereda de la clase padre Marino
    def hablar(self): # Método modificado en la clase hija
        print("Hola, soy un pulpo!")

class Foca(Marino): # Clase hija que hereda de la clase padre Marino
    def __init__(self, mensaje):    # Método modificado en la clase hija con un nuevo atributo
        self.mensaje = mensaje # Asignación del nuevo atributo
        
    def hablar(self): # Método modificado en la clase hija con el nuevo atributo
        print(self.mensaje)
        
marino = Marino()
marino.hablar()
pulpo = Pulpo()
pulpo.hablar()
foca = Foca("Hola, soy una foca!")
foca.hablar()   
