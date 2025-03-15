"""
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio; 
luego crear dos clases más que hereden de Fabrica, las cuales son Moto y Carro.
Crear métodos que muestren la cantidad de llantas, color y precio de ambos transportes. 
Por último, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno.
"""

class Fabrica():
    def __init__(self, llanta, color, precio):
        self.llanta = llanta
        self.color = color
        self.precio = precio

class Moto(Fabrica):
    def cantidad(self):
        print(f"Cantidad de llantas: {self.llanta}, Color: {self.color}, Precio: ${self.precio}")
        
class Carro(Fabrica):
    def cantidad(self):
        print(f"Cantidad de llantas: {self.llanta}, Color: {self.color}, Precio: ${self.precio}")


        
moto = Moto(2, "Rojo", 15000)
carro = Carro(4, "Negro", 30000)
moto.cantidad()
carro.cantidad()

