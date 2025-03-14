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
"""
Crear una clase Restaurante que tenga los atributos Nombre, Especialidad, Turnos
Crear una clase Cliente que tenga los atributos Nombre, Reserva 

Crear una funcion que al realizar una reserva comprueba si en la lista_restaurantes el restaurante existe, si no le indica que lo sentimos pero el restaurante no existe
si el restaurante exite en la lista_restaurantes busca en el Objeto el valor de turnos y los muestra en pantalla para que lo pueda elegir el cliente.
con la elecicion del cliente crea el objeto cliente con la reserva y suma 1 al turno de restaurante al llegar a 3 dice ese horario esta lleno.
"""

class Restaurante:
    def __init__(self, nombre, especialidad, turnos):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos = turnos
        self.dic_reserva = {turno: [] for turno in turnos}

    def mostrar_turnos(self):
        return self.turnos

    def realizar_reserva(self, cliente):
        turno = cliente.reserva
        if turno in self.turnos:
            if len(self.dic_reserva[turno]) < 3:
                self.dic_reserva[turno].append(cliente.nombre)
                print(f"Reserva realizada por {cliente.nombre} en el turno {turno}.")
            else:
                print(f"No se ha podido realizar la reserva. Pruebe en otro turno.")
        else:
            print(f"Turno {turno} no disponible.")

    def revisar_reservas(self):
        print("\nReservas actuales:")
        for turno, clientes in self.dic_reserva.items():
            disponibles = 3 - len(clientes)
            print(f"Turno {turno}: {clientes} (Disponibles: {disponibles})")
        print()

class Cliente:
    def __init__(self, nombre, reserva):
        self.nombre = nombre
        self.reserva = reserva

def realizar_reserva(lista_restaurantes):
    print("Restaurantes disponibles:")
    for i, restaurante in enumerate(lista_restaurantes):
        print(f"{i + 1}. {restaurante.nombre} - {restaurante.especialidad}")
    
    indice_restaurante = int(input("Elige el número del restaurante: ").strip()) - 1
    if 0 <= indice_restaurante < len(lista_restaurantes):
        restaurante = lista_restaurantes[indice_restaurante]
        nombre_cliente = input("Introduce tu nombre: ").strip()
        print(f"Turnos disponibles: {restaurante.mostrar_turnos()}")
        turno = int(input("Introduce el turno en el que deseas reservar: ").strip())
        cliente = Cliente(nombre_cliente, turno)
        restaurante.realizar_reserva(cliente)
    else:
        print("Opción no válida. Por favor, elige un restaurante de la lista.")

def revisar_reservas(lista_restaurantes):
    print("Restaurantes disponibles:")
    for i, restaurante in enumerate(lista_restaurantes):
        print(f"{i + 1}. {restaurante.nombre} - {restaurante.especialidad}")
    
    indice_restaurante = int(input("Elige el número del restaurante: ").strip()) - 1
    if 0 <= indice_restaurante < len(lista_restaurantes):
        restaurante = lista_restaurantes[indice_restaurante]
        restaurante.revisar_reservas()
    else:
        print("Opción no válida. Por favor, elige un restaurante de la lista.")

def mostrar_menu(lista_restaurantes):
    while True:
        print("\nMenú:")
        print("1. Realizar una reserva")
        print("2. Revisar reservas del restaurante")
        print("3. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            realizar_reserva(lista_restaurantes)
        elif opcion == "2":
            revisar_reservas(lista_restaurantes)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 3.")

# Ejemplo de uso
restaurante_1 = Restaurante("Can Pizza", "Cocina Italiana", (13, 14, 15, 20, 21, 22))
restaurante_2 = Restaurante("Sushi House", "Cocina Japonesa", (12, 13, 14, 19, 20, 21))
lista_restaurantes = [restaurante_1, restaurante_2]

# Mostrar el menú
mostrar_menu(lista_restaurantes)







