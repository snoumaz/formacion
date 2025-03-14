"""
Vamos a gestionar restaurantes. (Objetos)
Cada uno tiene: (atributos)
-- Nombre
-- Especialidad
-- Turnos 
    -- Puede hacer como maximo 3 clientes por turnos
    -- Si se  realiza la reserva diremos " Reserva realizada por {cliente}"
    -- Y si no "No se ha podido realizar las reserva. pruebe en otro truno"
-- Clientes

Clientes vamos a necesitar ( de momento)
-- Nombre

ejemplo de uso:
cliente_1 = Cliente("Anna")
restaurante_1 = Restaurante("Can Pizza","Cocina Italiana",(13,14,15,20,21,22))
"""

class Restaurante(): # Creacion de la clase
    #dic_turno = {}
    def __init__(self, nombre, especialidad, turnos): # Principales atributos 
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        self.dic_turno = {} # Atributo oculto que crea un diccionario vacio
        for hora in turnos: # Para la hora en turnos, 
            self.dic_turno[hora]=0 # crea la clave con el valor de turno y le deja el valor a 0
        
    def reserva(self,cliente,hora): # Crea el metodo reserva 
        if hora not in self.turnos: # Si la hora facilitada por el cliente no esta 
            return "no esta" # Printa el mensaje
        if self.dic_turno[hora] < 3: # Si el valor de la clave hora es menor a 3
            self.dic_turno[hora] += 1 # sumale el valor 
            return f"Reserva realizada por {cliente.name}"
        else:
            return "No se ha podido realizar la reserva. Pruebe en otro turno"

class Cliente():
    def __init__(self,name):
        self.name = name
        

cliente_1 = Cliente("Anna")
restaurante_1 = Restaurante("Can Pizza","Cocina Italiana",(13,14,15,20,21,22))

print(restaurante_1.reserva(cliente_1,13))
