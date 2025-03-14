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

# Creacion de la Clase Cliente

class Cliente(): 
    # Creacion del constructor
    def __init__(self, nombre):
        self.nombre = nombre

# Creacion objeto Cliente
anna = Cliente("Anna")
paco = Cliente("Paco")
pepe = Cliente("Pepe")
fran = Cliente("Fran")

# Creación de la Clase Restaurante

class Restaurante():
    """Atributos del Restaurante:\n
    Nombre\n
    Especialidad\n
    Turnos\n
    """
    def __init__(self, nombre:str, especialidad:str, turnos:tuple): # Metodo __init__ ( Metodo magico, constructor) define los atributos (nombre, espe, turnos)
        self.nombre = nombre # define el atributo nombre
        self.especialidad = especialidad # define el atributo espe
        self.turnos = turnos # define el atributo turnos
        self.reservas = {} # crea un atributo oculto que se define en el objeto creado , atributo para el control de los turnos
        for turno in turnos:
            self.reservas[turno] = 0
    
    # Creacion del metodo Reserva
    def reservar(self, cliente, hora_reserva):
        # Comprobar si la hora solicitada esta en los turnos disponibles
        if hora_reserva not in self.turnos:
            lista_turnos = [str(turno) for turno in self.turnos]
            mensaje = f"Lo sentimos no es posible la reserva a la {hora_reserva}.\n"
            mensaje += f"Nuestros horarios disponibles son: " + ", ".join(lista_turnos) + " horas"
            return mensaje
        # Comprobar la reserva anteriores
        if self.reservas[hora_reserva] < 3:
            self.reservas[hora_reserva] += 1
            return f"Reserva confirmada a las {hora_reserva} para el {cliente.nombre}"  
        else:
            return f"Lo sentimos, no es posible reservar a las {hora_reserva}. Hora esta completa."




# Creación de los objeto Restaurante

napoli = Restaurante("Napoli","Cocina Italiana",(12,13,14,15,20,21,22))

# print(napoli.__doc__) # __doc__ nos muestra la documentacion
# print(napoli.__dict__) #  __dict__ nos da enforma diccionario los atributos del objeto 

print(napoli.reservar(anna, 14))
print(napoli.reservar(anna, 14))
print(napoli.reservar(anna, 14))
print(napoli.reservar(anna, 14))