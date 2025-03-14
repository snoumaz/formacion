import random

class Cliente:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class CuentaBancaria:
    def __init__(self, titulares):
        self.titulares = titulares  # Lista de clientes
        self.saldo = 0.0
        self.numero_cuenta = random.randint(100000, 999999)
    
    def ingresar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Se han depositado {cantidad}€ en la cuenta {self.numero_cuenta}.")
        else:
            print("La cantidad a ingresar debe ser mayor que cero.")

    def retirar_dinero(self, cantidad):
        if cantidad > 0:
            if self.saldo >= cantidad:
                self.saldo -= cantidad
                print(f"Se han retirado {cantidad}€ de la cuenta {self.numero_cuenta}. Saldo actual: {self.saldo}€")
            else:
                print("Saldo insuficiente.")
        else:
            print("La cantidad a retirar debe ser mayor que cero.")
    
    def mostrar_saldo_cliente(self):
        titulares_nombres = ", ".join([f"{titular.nombre} {titular.apellido}" for titular in self.titulares])
        print(f"Cuenta | Titulares | Saldo\n{self.numero_cuenta} | {titulares_nombres} | {self.saldo}€")

class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []
    
    def crear_cuenta(self, clientes):
        cuenta = CuentaBancaria(clientes)
        self.cuentas.append(cuenta)
        titulares_nombres = ", ".join([f"{cliente.nombre} {cliente.apellido}" for cliente in clientes])
        print(f"Cuenta creada para {titulares_nombres} con número {cuenta.numero_cuenta}.")
    
    def eliminar_cuenta(self, numero_cuenta):
        for cuenta in self.cuentas:
            if cuenta.numero_cuenta == numero_cuenta:
                self.cuentas.remove(cuenta)
                print(f"Cuenta {numero_cuenta} eliminada del banco.")
                return
        print("Cuenta no encontrada.")
    
    def mostrar_cuentas(self):
        print(f"Banco {self.nombre}\n==============================")
        print("Cuenta | Titulares | Saldo")
        total_depositos = sum(cuenta.saldo for cuenta in self.cuentas)
        for cuenta in self.cuentas:
            titulares_nombres = ", ".join([f"{titular.nombre} {titular.apellido}" for titular in cuenta.titulares])
            print(f"{cuenta.numero_cuenta} | {titulares_nombres} | {cuenta.saldo}€")
        print(f"Total depósitos: {total_depositos}€\n==============================")

# Creación del banco
banco = Banco("Pasta Bank")

# Creación de clientes
clientes = [
    Cliente("María", "Gómez", 30),
    Cliente("Joan", "Pérez", 40),
    Cliente("Ana", "López", 35),
    Cliente("Carlos", "Ruiz", 50),
    Cliente("Lucía", "Fernández", 28)
]

# Creación de cuentas con múltiples titulares
banco.crear_cuenta([clientes[0], clientes[1]])
banco.crear_cuenta([clientes[2]])
banco.crear_cuenta([clientes[3], clientes[4]])

# Operaciones de prueba
banco.cuentas[0].ingresar_dinero(500)
banco.cuentas[1].ingresar_dinero(4000)
banco.cuentas[2].ingresar_dinero(1500)

banco.cuentas[1].retirar_dinero(300)
banco.cuentas[2].retirar_dinero(500)

banco.mostrar_cuentas()

banco.eliminar_cuenta(banco.cuentas[1].numero_cuenta)
banco.mostrar_cuentas()