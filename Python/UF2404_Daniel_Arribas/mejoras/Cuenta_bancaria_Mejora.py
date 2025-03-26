"""
Programación orientada a objetos: Gestión de cuentas bancarias.

El programa debe:

    Definir la clase Cliente, con los atributos nombre, apellido y edad.

    Definir la clase Banco, con el atributo nombre.
    Incluiremos un método "crear_cuenta" para añadir cuentas.
    Incluiremos un método "eliminar_cuenta" para quitarla del banco.
    Incluiremos el método "mostrar_cuentas" para obtener los datos
    de las diferentes cuentas y el total ingresado en el banco. Ejemplo:
    
    Banco Pasta Bank
    ==============================
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    295310 | Joan    | 4000€
    Total depósitos: 4500.0€
    ==============================


    Definir la clase CuentaBancaria con los atributos titular y saldo.
    Al crear la cuenta bancaria el saldo será 0.
    Incluiremos un número de cuenta mediante un número aleatorio entre
    100000 y 999999.

    Incluir un método ingresar_dinero(...) que permita añadir dinero a la cuenta.
    Deben ser cantidades positivas mayores que cero. En caso contrario mostrar el aviso.
    El mensaje de salida será:
    "Se han depositado [cantidad]€ en la cuenta de [nombre_del_cliente]"

    Incluir un método retirar_dinero(...) que permita retirar dinero de la cuenta, 
    si hay suficiente saldo para ello. En caso contrario, 
    mostrar un mensaje de saldo insuficiente.
    Ejemplo de mensaje: 
    "Se han retirado [cantidad]€ de la cuenta de [nombre_del_cliente]. 
    Saldo actual: [saldo]€"
    Hay que verificar que la cantidad a retirar sea positiva mayor que cero.

    Incluir un método mostrar_saldo_cliente(...) que muestre el saldo actual.
    Así:
    Cuenta | Titular | Saldo
    159142 | María   | 500.0€
    
     
    Crear al menos 5 cuentas bancarias y utilizar todos 
    los métodos de cada una.

    Nota: no hace falta crear inputs para la entrada de datos.
    Se pueden utilizar directamente los métodos.
"""
import random # Importar la librería random para generar números aleatorios.

# Definir la clase Cliente, con los atributos nombre, apellido y edad.
class Cliente():
    """
    Clase Cliente con atributos:\n
    - nombre: str\n
    - apellido: str\n
    - edad: int\n
    """
    def __init__(self, nombre, apellido, edad): # Constructor del cliente con nombre, apellido y edad.
        self.nombre = nombre # Atributo nombre
        self.apellido = apellido # Atributo apellido
        self.edad = edad # Atributo edad
    def __str__(self): # Método para mostrar el cliente.
        return f"Cliente {self.nombre} {self.apellido} de {self.edad} años." # Devuelve el nombre, apellido y edad del cliente.
    
# Definir la clase Banco, con el atributo nombre.
class Banco():
    """
    Clase Banco con atributos:\n
    - Nombre: str\n
    - Cuentas: list\n
    """
    def __init__(self, nombre): # Constructor del banco con el nombre.
        self.nombre = nombre # Atributo nombre
        self.cuentas = [] # Atributo cuentas

    def __str__(self): # Método para mostrar el banco.
        return f"Banco {self.nombre}" # Devuelve el nombre del banco.
    
    def crear_cuenta(self, nombre, apellido, edad): # Método para crear una cuenta bancaria.
        """
        Metodo para crear una cuenta bancaria.\n
        - nombre: str\n
        - apellido: str\n
        - edad: int\n
        """
        for cuenta in self.cuentas: # Para el objeto CuentaBancaria en la lista de cuentas
            if cuenta.cliente.nombre == nombre and cuenta.cliente.apellido == apellido: # Si el nombre y el apellido estan en la lista 
                return "Cliente ya existe" # informa de que el Cliente ya existe

        # Si no existe, se agrega
        nuevo_cliente = Cliente(nombre, apellido, edad) # Crea un nuevo objeto Cliente con los datos
        nueva_cuenta = CuentaBancaria(nuevo_cliente) # Crea una nueva cuenta bancaria con el cliente
        self.cuentas.append(nueva_cuenta) # añade a la lista cuentas la nueva cuenta bancaria
        return "Cliente agregado con éxito" # Muestra en pantalla el mensaje
    
    def eliminar_cuenta(self, nombre, apellido): # Método para eliminar una cuenta bancaria.
        """
        Metodo para eliminar una cuenta bancaria.\n
        - nombre: str\n
        - apellido: str\n
        """
        for cuenta in self.cuentas: # Para el objeto CuentaBancaria en la lista de cuentas
            if cuenta.cliente.nombre == nombre and cuenta.cliente.apellido == apellido: # Si el nombre y el apellido estan en la lista
                self.cuentas.remove(cuenta) # Elimina el Cliente de la lista
                return "Cliente eliminado con éxito" # Muestra en pantalla el mensaje de eliminación
        return "Cliente no encontrado" # Muestra en pantalla el mensaje de no encontrado el cliente
    
    def mostrar_cuentas(self): # Método para mostrar las cuentas bancarias.
        """
        Metodo para mostrar las cuentas bancarias.\n
        """
        total_depositos = 0 # Variable para el total de depósitos
        print("="*30) # Muestra en pantalla una línea de 30 caracteres
        print(f"{self.nombre}") # Muestra en pantalla el nombre del banco
        print("="*30) # Muestra en pantalla una línea de 30 caracteres          
        print(f"{'Cuenta':<10} | {'Titular':<20} | {'Saldo':>10}") # Muestra en pantalla los títulos de las columnas
        for cuenta in self.cuentas: # Para el objeto CuentaBancaria en la lista de cuentas
            print(cuenta) # Muestra en pantalla la cuenta
            total_depositos += cuenta.saldo # Suma el saldo de la cuenta al total de depósitos
        print(f"Total depósitos: {total_depositos:.2f}€") # Muestra en pantalla el total de depósitos
        print("="*30) # Muestra en pantalla una línea de 30 caracteres


# Definir la clase CuentaBancaria con los atributos titular y saldo.
class CuentaBancaria(): 
    """
    Clase CuentaBancaria con atributos:\n
    - cliente: Cliente\n
    - saldo: float\n
    - numero_cuenta: int\n
    """
    def __init__(self, cliente, saldo=0): # Constructor de la cuenta bancaria con el cliente y saldo.
        self.cliente = cliente # Atributo cliente
        self.saldo = saldo # Atributo saldo
        self.numero_cuenta = random.randint(100000, 999999) # Atributo número de cuenta aleatorio entre 100000 y 999999.
    
    def __str__(self): # Método para mostrar la cuenta bancaria.
        return f"{self.numero_cuenta:<10} | {self.cliente.nombre} {self.cliente.apellido:<20} | {self.saldo:>10.2f}€" # Devuelve el número de cuenta, nombre, apellido y saldo de la cuenta.
    
    def ingresar_dinero(self, cantidad): # Método para ingresar dinero en la cuenta.
        """
        Metodo para ingresar dinero en la cuenta.\n
        - cantidad: float\n
        """
        if cantidad > 0: # Si la cantidad es mayor que cero
            self.saldo += cantidad # Suma la cantidad al saldo
            print(f"Se han depositado {cantidad:.2f}€ en la cuenta de {self.cliente.nombre} {self.cliente.apellido}") # Muestra en pantalla el mensaje
        else: # Si la cantidad es menor o igual a cero
            print("La cantidad a ingresar debe ser mayor que cero.") # Muestra en pantalla el mensaje
    
    def retirar_dinero(self, cantidad): # Método para retirar dinero de la cuenta.
        """
        Metodo para retirar dinero de la cuenta.\n
        - cantidad: float\n
        """
        if cantidad > 0: # Si la cantidad es mayor que cero
            if self.saldo >= cantidad: # Si el saldo es mayor o igual a la cantidad
                self.saldo -= cantidad  # Resta la cantidad al saldo
                print(f"Se han retirado {cantidad:.2f}€ de la cuenta de {self.cliente.nombre} {self.cliente.apellido}. Saldo actual: {self.saldo:.2f}€") # Muestra en pantalla el mensaje
            else: # Si el saldo es menor que la cantidad
                print("Saldo insuficiente.") # Muestra en pantalla el mensaje
        else:   # Si la cantidad es menor o igual a cero
            print("La cantidad a retirar debe ser mayor que cero.") # Muestra en pantalla el mensaje
    
    def mostrar_saldo_cliente(self): # Método para mostrar el saldo del cliente.
        """
        Metodo para mostrar el saldo del cliente.\n
        """
        print("="*30)
        print(f"Numero de cuenta:\n{self.numero_cuenta}\n\nTitular de la Cuenta:\n{self.cliente.nombre} {self.cliente.apellido}\n\nSaldo disponible:\n{self.saldo:.2f}€") # Muestra en pantalla el número de cuenta, nombre, apellido y saldo de la cuenta.
        print("="*30)

print("Ejemplo de uso de las clases:")
# Crear un banco
banco = Banco("Pasta Bank")
print(banco)

# Crear cuentas
print(banco.crear_cuenta("Maria", "Perez", 30))
print(banco.crear_cuenta("Joan", "Pradells", 40))
banco.mostrar_cuentas()

# Ingresar dinero
banco.cuentas[0].ingresar_dinero(500)
banco.cuentas[1].ingresar_dinero(4000)
banco.mostrar_cuentas()

# Retirar dinero
banco.cuentas[0].retirar_dinero(100)
banco.cuentas[1].retirar_dinero(5000)
banco.mostrar_cuentas()

# Eliminar cuenta
print(banco.eliminar_cuenta("Maria", "Perez"))
banco.mostrar_cuentas()

# Crear más cuentas
print(banco.crear_cuenta("Luis", "Garcia", 25))
print(banco.crear_cuenta("Ana", "Martinez", 35))
print(banco.crear_cuenta("Carlos", "Lopez", 45))
banco.mostrar_cuentas()

# mostrar saldo de un cliente
banco.cuentas[0].mostrar_saldo_cliente()

