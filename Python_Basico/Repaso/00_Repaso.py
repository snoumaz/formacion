"""
Repaso conceptos Basicos de python     
"""

# Variables y tipos de datos
entero = 5 # Variable entera
string = "Hola" # Variable cadena de texto (string)
flotante = 3.14 # Variable flotante (decimal)
booleando = True # Variable booleana (verdadero o falso)
introduccion = input("Introduce tu nombre: ") # Input para introducir datos por parte del usuario
print(introduccion) # Imprimir el dato introducido por el usuario

# Todos los valores string se pueden tratar con diferentes metodos.
string = "Hola Mundo"
print(string.upper()) # Convertir a mayusculas
print(string.lower()) # Convertir a minusculas
print(string.capitalize()) # Capitalizar la primera letra del string
print(string.replace("Mundo", "Python")) # Reemplazar una parte del string por otra
print(len(string)) # Longitud del string
print(string[0]) # Acceder al primer caracter del string (index 0)
print(string[-1]) # Acceder al último caracter del string (index -1)

# Operaciones matemáticas básicas
suma = entero + flotante # Suma de dos variables con diferentes tipos de datos
resta = entero - flotante # Resta de dos variables con diferentes tipos de datos
multiplicacion = entero * flotante # Multiplicación de dos variables con diferentes tipos de datos
division = entero / flotante # División de dos variables con diferentes tipos de datos
modulo = entero % flotante # Módulo (resto de la división) de dos variables con diferentes tipos de datos
potencia = entero ** flotante # Potenciación de dos variables con diferentes tipos de datos
raiz_cuadrada = entero ** 0.5  # Raíz cuadrada de un número
print(suma, resta, multiplicacion, division, modulo, potencia, raiz_cuadrada)

# Operaciones lógicas básicas
and_logico = True and False # AND lógico entre dos valores booleanos
or_logico = True or False # OR lógico entre dos valores booleanos
not_logico = not True # NOT lógico de un valor booleano
print(and_logico, or_logico, not_logico)

# Operaciones relacionales básicas
igualdad = entero == flotante # Igualdad entre dos variables con diferentes tipos de datos
desigualdad = entero != flotante # Desigualdad entre dos variables con diferentes tipos de datos
mayor_que = entero > flotante # Mayor que entre dos variables con diferentes tipos de datos
menor_que = entero < flotante # Menor que entre dos variables con diferentes tipos de datos
mayor_igual = entero >= flotante # Mayor o igual que entre dos variables con diferentes tipos de datos
menor_igual = entero <= flotante # Menor o igual que entre dos variables con diferentes tipos de datos
print(igualdad, desigualdad, mayor_que, menor_que, mayor_igual, menor_igual)

# Condicionales simples y compuestas
numero = 10 # Asignación de un valor entero a la variable 'numero'
if numero > 5: # Si el valor de 'numero' es mayor que 5, se ejecuta el bloque de código dentro del if
    print("El número es mayor que 5") # Imprime "El número es mayor que 5" en la consola
elif numero == 5: # Si el valor de 'numero' es igual a 5, se ejecuta el bloque de código dentro del elif
    print("El número es igual a 5") # Imprime "El número es igual a 5" en la consola
else: # Si ninguna de las condiciones anteriores se cumple, se ejecuta el bloque de código dentro del else
    print("El número es menor que 5") # Imprime "El número es menor que 5" en la consola

# Bucles for y while
# Bucle for con range()
for i in range(5): # Crea un bucle for que itera desde 0 hasta 4 (inclusive)
    print(i) # Imprime el valor de 'i' en la consola
# Bucle while con incremento manual
j = 0 # Asignación de un valor entero a la variable 'j'
while j < 5: # Crea un bucle while que itera mientras 'j' sea menor que 5
    print(j) # Imprime el valor de 'j' en la consola
    j += 1 # Incrementa el valor de 'j' en 1

# Listas
mi_lista = [1, 2, 3, 4, 5] # Crea una lista llamada 'mi_lista' con cinco elementos enteros
for elemento in mi_lista: # Crea un bucle for que itera sobre cada elemento de 'mi_lista'
    print(elemento) # Imprime el valor del elemento en la consola

# Diccionarios
mi_diccionario = {'nombre': 'Juan', 'edad': 25} # Crea un diccionario llamado 'mi_diccionario' con dos claves y valores correspondientes
for clave, valor in mi_diccionario.items(): # Crea un bucle for que itera sobre cada par clave-valor del diccionario
    print(clave, valor) # Imprime la clave y el valor del par en la consola

# Tuplas
mi_tupla = (1, 2, 3) # Crea una tupla llamada 'mi_tupla' con tres elementos enteros
for elemento in mi_tupla: # Crea un bucle for que itera sobre cada elemento de 'mi_tupla'
    print(elemento) # Imprime el valor del elemento en la consola
    
# Funciones
def suma(a, b): # Define una función llamada 'suma' que toma dos parámetros: 'a' y 'b'
    return a + b # Devuelve la suma de 'a' y 'b'
resultado = suma(3, 4) # Llama a la función 'suma' con los argumentos 3 y 4 y asigna el resultado a la variable 'resultado'
print(resultado) # Imprime el valor de 'resultado' en la consola

# Clases y Objetos
class Persona(): # Define una clase llamada 'Persona'
    def __init__(self, nombre, edad): # Define un método constructor que toma dos parámetros: 'nombre' y 'edad'
        self.nombre = nombre # Asigna el valor de 'nombre' al atributo 'nombre' del objeto
        self.edad = edad # Asigna el valor de 'edad' al atributo 'edad' del objeto
    def presentarse(self): # Define un método llamado 'presentarse'
        return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años." # Devuelve una cadena que presenta el objeto
persona1 = Persona("Juan", 25) # Crea un objeto de la clase 'Persona' con el nombre "Juan" y la edad 25 y lo asigna a la variable 'persona1'
print(persona1.presentarse()) # Imprime el resultado del método 'presentarse' del objeto 'persona1' en la consola
# Las classe pueden tener atributos y métodos. Los atributos son variables que almacenan datos sobre el objeto, mientras que los métodos son funciones que definen el comportamiento del objeto.
# Tambien pueden tener subclases, que son clases que heredan de otras clases. Las subclases pueden agregar nuevos atributos y métodos o sobrescribir los existentes.

class Estudiante(Persona): # Define una subclase llamada 'Estudiante' que hereda de la clase 'Persona'
    def __init__(self, nombre, edad, matricula): # Define un método constructor que toma tres parámetros: 'nombre', 'edad' y 'matricula'
        super().__init__(nombre, edad) # Llama al constructor de la clase padre ('Persona') y pasa los parámetros 'nombre' y 'edad' a él.
        self.matricula = matricula # Asigna el valor del parámetro 'matricula' al atributo 'matricula' del objeto.
    def presentarse(self): # Define un método llamado 'presentarse'
        return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y mi matrícula es {self.matricula}" # Devuelve una cadena de texto que presenta el objeto.
    def estudiar(self, materia): # Define un método llamado 'estudiar' que toma un parámetro: 'materia'
        return f"{self.nombre} está estudiando {materia}" # Devuelve una cadena de texto que indica que el objeto está estudiando la materia especificada.
    def __str__(self): # Define un método mágico llamado '__str__' que se ejecuta cuando se intenta convertir el objeto a una cadena de texto.
        return f"{self.nombre} ({self.edad}) - Matrícula: {self.matricula}" # Devuelve una cadena de texto que representa el objeto en formato legible.

# Creación de objetos

persona1 = Estudiante("Juan", 20, "123456789") # Crea un objeto de la clase 'Estudiante' con el nombre "Juan", edad 20 y matrícula "123456789".
persona2 = Estudiante("María", 22, "987654321") # Crea otro objeto de la clase 'Estudiante' con el nombre "María", edad 22 y matrícula "987654321".

# Métodos de instancia

def presentarse(self): # Define un método de instancia llamado 'presentarse' que toma como parámetro el objeto actual ('self').
    return f"Hola, mi nombre es {self.nombre}, tengo {self.edad} años y mi matrícula es {self.matricula}" # Devuelve una cadena de texto que presenta al estudiante.
Estudiante.presentarse = presentarse # Asigna el método 'presentarse' a la clase 'Estudiante'.

# Valores predeterminados

__name__ == "__main__": # type: ignore # Comprueba si el archivo se está ejecutando como el programa principal.
print("Este es un ejemplo de una clase en Python.") # Imprime un mensaje en la consola
print(persona1.presentarse()) # Imprime el resultado del método 'presentarse' del objeto 'persona1' en la consola
  
__token = "your_token_here" # Define una variable con un valor predeterminado inmutable.

