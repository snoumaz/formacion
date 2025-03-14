# Este proyecto es de practica para rememorar los conceptos básicos de Python. o

# Variables de diferentes tipos de datos, operaciones y métodos de comparación, conversión y manipulación de cadenas / strings y listas

variable = 2 # Variable de tipo entero
variable2 = 2.5 # Variable de tipo flotante
variable3 = "Hola, mundo!" # Variable de tipo cadena / string
variable4 = True # Variable de tipo booleano
variable5 = None # Variable de tipo nulo
variable6 = input("Ingresa un número: ") # Variable de tipo cadena / string / input al usuario
variable7 = int(variable6) # Convertir variable6 a entero
variable8 = float(variable6) # Convertir variable6 a flotante
variable9 = str(variable) # Convertir variable a cadena / string
variable10 = bool(variable) # Convertir variable a booleano
variable11 = input("Ingresa un texto: ") # Variable de tipo cadena / string / input al usuario
variable12 = variable11.split() # Convertir variable11 a lista
variable13 = " ".join(variable12) # Convertir variable12 a cadena / string
variable14 = variable11.upper() # Convertir variable11 a mayúsculas
variable15 = variable11.lower() # Convertir variable11 a minúsculas
variable16 = variable11.capitalize() # Convertir variable11 a capitalizado
variable17 = variable11.title() # Convertir variable11 a título
variable18 = variable11.strip() # Eliminar espacios en blanco al inicio y al final
variable19 = variable11.replace("a", "e") # Reemplazar caracteres
variable20 = variable11.find("a") # Encontrar la posición de un caracter
variable21 = variable11.count("a") # Contar la cantidad de un caracter
variable22 = variable11.startswith("H") # Verificar si la cadena inicia con un caracter
variable23 = variable11.endswith("o") # Verificar si la cadena termina con un caracter
variable24 = len(variable11) # Longitud de la cadena / cantidad de caracteres del texto
variable25 = variable11[0] # Obtener el primer caracter
variable26 = variable11[-1] # Obtener el último caracter
variable27 = variable11[1:3] # Obtener un rango de caracteres
variable28 = variable11[::-1] # Invertir la cadena
variable29 = variable + variable6 # Concatenar cadenas / sumar números
variable30 = variable * 3 # Multiplicar cadenas / números por un número entero
variable31 = variable.isdigit() # Verificar si la cadena es un número
variable32 = variable.isalpha() # Verificar si la cadena es una letra
variable33 = variable.isalnum() # Verificar si la cadena es un número o una letra
variable34 = variable.isupper() # Verificar si la cadena está en mayúsculas
variable35 = variable.islower() # Verificar si la cadena está en minúsculas
variable36 = variable.isnumeric() # Verificar si la cadena es numérica
variable37 = variable.isdecimal() # Verificar si la cadena es decimal
variable38 = variable.isidentifier() # Verificar si la cadena es un identificador 
variable39 = variable.isprintable() # Verificar si la cadena es imprimible
variable40 = variable.isascii() # Verificar si la cadena es ASCII
variable41 = variable.isalnum() # Verificar si la cadena es alfanumérica

print(variable) # Imprimir variable


# Listas de diferentes tipos de datos, operaciones y métodos de comparación, conversión y manipulación de listas

lista = [1, 2, 3, 4, 5] # Lista de enteros
lista2 = [1, 2.5, "Hola", True, None] # Lista de diferentes tipos de datos
lista3 = [] # Lista vacía
lista4 = list(range(5)) # Lista de un rango de números
lista5 = list("Hola, mundo!") # Lista de caracteres
lista6 = lista + lista4 # Concatenar listas
lista7 = lista.append(6) # Agregar un elemento a la lista
lista8 = lista.insert(0, 0) # Insertar un elemento en la posición 0
lista9 = lista.pop() # Eliminar el último elemento de la lista
lista10 = lista.remove(0) # Eliminar el elemento 0 de la lista
lista11 = lista.clear() # Limpiar la lista
lista12 = lista.copy() # Copiar la lista
lista13 = lista.count(1) # Contar la cantidad de elementos 1 en la lista
lista14 = lista.index(1) # Encontrar la posición del elemento 1 en la lista
lista15 = lista.reverse() # Invertir la lista
lista16 = lista.sort() # Ordenar la lista
lista17 = lista.extend(lista4) # Extender la lista con otra lista
lista18 = lista[0] # Obtener el primer elemento
lista19 = lista[-1] # Obtener el último elemento
lista20 = lista[1:3] # Obtener un rango de elementos
lista21 = lista[::-1] # Invertir la lista
lista22 = len(lista) # Longitud de la lista / cantidad de elementos de la lista
lista23 = lista.extend([6, 7, 8]) # Extender la lista con elementos

print(lista) # Imprimir lista

# Condicionales, ciclos y estructuras de control

if variable == 2: # Condición if / si variable es igual a 2 entonces continua
    print("La variable es igual a 2.")
elif variable > 2: # Condición elif / si variable es mayor a 2 entonces continua
    print("La variable es mayor a 2.")
else: # Condición else / si ninguna de las anteriores se cumple entonces continua
    print("La variable es menor a 2.")

for busca in lista: # Ciclo for / para cada elemento en la lista
    print(busca) # Imprimir el elemento
    if busca == 2: # Condición if / si busca es igual a 2 entonces continua
            print("El elemento es igual a 2.")
    elif busca > 2: # Condición elif / si busca es mayor a 2 entonces continua
            print("El elemento es mayor a 2.")
    else: # Condición else / si ninguna de las anteriores se cumple entonces continua
            print("El elemento es menor a 2.")


# Ciclos for y while, estructuras match y try

for i in range(5): # Ciclo for / para cada número en el rango de 0 a 4
    print(i) # Imprimir el número

for i in range(1, 6): # Ciclo for / para cada número en el rango de 1 a 5
    print(i) # Imprimir el número
    
for i in range(0, 10, 2): # Ciclo for / para cada número en el rango de 0 a 9 con un paso de 2
    print(i) # Imprimir el número
    
for i in range(10, 0, -1): # Ciclo for / para cada número en el rango de 10 a 1 con un paso de -1
    print(i) # Imprimir el número

while variable < 5: # Ciclo while / mientras variable sea menor a 5 entonces continua
    print(variable) # Imprimir variable
    variable += 1 # Incrementar variable en 1

while True: # Ciclo while / mientras sea verdadero entonces continua
    variable = input("Ingresa un número: ") # Variable de tipo cadena / string / input al usuario
    if variable == "salir": # Condición if / si variable es igual a "salir" entonces continua
        break # Interrumpir el ciclo
    print(variable) # Imprimir variable

match variable: # Estructura match / comparar variable con los siguientes casos
    case 1: # Caso 1
        print("La variable es igual a 1.")
    case 2: # Caso 2
        print("La variable es igual a 2.")
    case 3: # Caso 3
        print("La variable es igual a 3.")
    case _: # Caso por defecto
        print("La variable es diferente a 1, 2 y 3.")

try: # Estructura try / intentar ejecutar el código
    print(variable) # Imprimir variable
except Exception as e: # Estructura except / si hay un error entonces continua
    print(f"Error: {e}") # Imprimir el error
except ValueError: # Estructura except / si hay un error de valor entonces continua
    print("Error de valor.") # Imprimir el error
except: # Estructura except / si hay un error entonces continua
    print("Error.") # Imprimir el error
finally: # Estructura finally / siempre se ejecuta al final
    print("Fin del programa.") # Imprimir el mensaje
    
    
# Diccioanrios, conjuntos y funciones

diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Lima"} # Diccionario de datos
diccionario2 = dict(nombre="Ana", edad=25, ciudad="Arequipa") # Diccionario de datos
diccionario3 = {} # Diccionario vacío
diccionario4 = dict(zip(["a", "b", "c"], [1, 2, 3])) # Diccionario de datos con zip de dos listas 
diccionario5 = dict([("a", 1), ("b", 2), ("c", 3)]) # Diccionario de datos con una lista de tuplas
diccionario6 = diccionario.copy() # Copiar el diccionario
diccionario7 = diccionario.get("nombre") # Obtener el valor de la clave "nombre"
diccionario8 = diccionario.pop("nombre") # Eliminar la clave "nombre" y obtener su valor
diccionario9 = diccionario.popitem() # Eliminar el último elemento y obtener su clave y valor
diccionario10 = diccionario.setdefault("nombre", "Pedro") # Obtener el valor de la clave "nombre" o establecerlo si no existe
diccionario11 = diccionario.update({"nombre": "Pedro"}) # Actualizar el valor de la clave "nombre"
diccionario12 = diccionario.keys() # Obtener las claves del diccionario
diccionario13 = diccionario.values() # Obtener los valores del diccionario 
diccionario14 = diccionario.items() # Obtener los elementos del diccionario como tuplas
diccionario15 = diccionario.clear() # Limpiar el diccionario
diccionario16 = len(diccionario) # Longitud del diccionario / cantidad de elementos del diccionario
diccionario17 = "nombre" in diccionario # Verificar si la clave "nombre" está en el diccionario
diccionario18 = "Juan" in diccionario.values() # Verificar si el valor "Juan" está en el diccionario
diccionarios = [diccionario, diccionario2] # Lista de diccionarios

print(diccionario) # Imprimir diccionario


# Conjuntos de diferentes tipos de datos, operaciones y métodos de comparación, conversión y manipulación de conjuntos

conjunto = {1, 2, 3, 4, 5} # Conjunto de números
conjunto2 = {1, 2.5, "Hola", True, None} # Conjunto de diferentes tipos de datos
conjunto3 = set() # Conjunto vacío
conjunto4 = set(range(5)) # Conjunto de un rango de números
conjunto5 = set("Hola, mundo!") # Conjunto de caracteres
conjunto6 = conjunto | conjunto4 # Unión de conjuntos
conjunto7 = conjunto & conjunto4 # Intersección de conjuntos
conjunto8 = conjunto - conjunto4 # Diferencia de conjuntos
conjunto9 = conjunto ^ conjunto4 # Diferencia simétrica de conjuntos
conjunto10 = conjunto.add(6) # Agregar un elemento al conjunto
conjunto11 = conjunto.remove(6) # Eliminar un elemento del conjunto
conjunto12 = conjunto.discard(6) # Eliminar un elemento del conjunto si existe
conjunto13 = conjunto.pop() # Eliminar un elemento del conjunto
conjunto14 = conjunto.clear() # Limpiar el conjunto
conjunto15 = conjunto.copy() # Copiar el conjunto
conjunto16 = len(conjunto) # Longitud del conjunto / cantidad de elementos del conjunto
conjunto17 = 1 in conjunto # Verificar si el elemento 1 está en el conjunto
conjunto18 = conjunto.isdisjoint(conjunto4) # Verificar si el conjunto es disjunto
conjunto19 = conjunto.issubset(conjunto4) # Verificar si el conjunto es subconjunto
conjunto20 = conjunto.issuperset(conjunto4) # Verificar si el conjunto es superconjunto 
conjuntos = [conjunto, conjunto2] # Lista de conjuntos

print(conjunto) # Imprimir conjunto


# Funciones de diferentes tipos de datos, operaciones y métodos de comparación, conversión y manipulación de funciones

def suma(a, b): # Función suma / sumar dos números
    return a + b # Retornar la suma de los números

def resta(a, b): # Función resta / restar dos números
    return a - b # Retornar la resta de los números

def multiplicacion(a, b): # Función multiplicación / multiplicar dos números
    return a * b # Retornar la multiplicación de los números

def division(a, b): # Función división / dividir dos números
    try: # Estructura try / intentar ejecutar el código
        return a / b # Retornar la división de los números
    except ZeroDivisionError: # Estructura except / si hay un error de división por cero entonces continua
        return "Error: división por cero." # Retornar el error
    
def potencia(a, b): # Función potencia / elevar un número a otro número
    return a ** b # Retornar la potencia de los números

def raiz(a): # Función raíz cuadrada / obtener la raíz cuadrada de un número
    return a ** 0.5 # Retornar la raíz cuadrada del número

def cuadrado(a): # Función cuadrado / elevar un número al cuadrado
    return a ** 2 # Retornar el cuadrado del número

def cubo(a): # Función cubo / elevar un número al cubo
    return a ** 3 # Retornar el cubo del número

def area_circulo(r): # Función área del círculo / obtener el área de un círculo
    return 3.1416 * r ** 2 # Retornar el área del círculo

def area_triangulo(b, h): # Función área del triángulo / obtener el área de un triángulo
    return (b * h) / 2 # Retornar el área del triángulo

def area_rectangulo(b, h): # Función área del rectángulo / obtener el área de un rectángulo
    return b * h # Retornar el área del rectángulo

def area_cuadrado(l): # Función área del cuadrado / obtener el área de un cuadrado
    return l ** 2 # Retornar el área del cuadrado

def area_cubo(l): # Función área del cubo / obtener el área de un cubo
    return 6 * l ** 2 # Retornar el área del cubo

def area_esfera(r): # Función área de la esfera / obtener el área de una esfera
    return 4 * 3.1416 * r ** 2 # Retornar el área de la esfera

def volumen_esfera(r): # Función volumen de la esfera / obtener el volumen de una esfera
    return (4 / 3) * 3.1416 * r ** 3 # Retornar el volumen de la esfera

def area_cilindro(r, h): # Función área del cilindro / obtener el área de un cilindro
    return (2 * 3.1416 * r * h) + (2 * 3.1416 * r ** 2) # Retornar el área del cilindro

def volumen_cilindro(r, h): # Función volumen del cilindro / obtener el volumen de un cilindro
    return 3.1416 * r ** 2 * h # Retornar el volumen del cilindro

def area_cono(r, g): # Función área del cono / obtener el área de un cono
    return 3.1416 * r * (r + g) # Retornar el área del cono

def volumen_cono(r, h): # Función volumen del cono / obtener el volumen de un cono
    return (1 / 3) * 3.1416 * r ** 2 * h # Retornar el volumen del cono

def area_piramide(b, h): # Función área de la pirámide / obtener el área de una pirámide
    return b + (b * h) # Retornar el área de la pirámide

def volumen_piramide(b, h): # Función volumen de la pirám
    return (1 / 3) * b * h # Retornar el volumen de la pirámide

def area_cuboide(l, a, p): # Función área del cuboide / obtener el área de un cuboide
    return 2 * (l * a + l * p + a * p) # Retornar el área del cuboide

def volumen_cuboide(l, a, p): # Función volumen del cuboide / obtener el volumen de un cuboide
    return l * a * p # Retornar el volumen del cuboide

def area_prisma(b, h): # Función área del prisma / obtener el área de un prisma
    return b * h # Retornar el área del prisma

def volumen_prisma(b, h): # Función volumen del prisma / obtener el volumen de un prisma
    return b * h # Retornar el volumen del prisma

def __init__(self, nombre, edad): # Método constructor / inicializar la clase
    self.nombre = nombre # Atributo nombre
    self.edad = edad # Atributo edad

def saludar(self): # Método saludar / saludar a la persona
    return f"Hola, me llamo {self.nombre} y tengo {self.edad} años." # Retornar el saludo

def despedir(self): # Método despedir / despedir a la persona
    return f"Adiós, me llamo {self.nombre} y tengo {self.edad} años." # Retornar la despedida

def __str__(self): # Método str / convertir la clase a cadena / string
    return f"Nombre: {self.nombre}, Edad: {self.edad}" # Retornar la cadena / string

def __del__(self): # Método del / eliminar la clase
    print(f"La persona {self.nombre} ha sido eliminada.") # Imprimir el mensaje

def __add__(self, other): # Método add / sumar dos clases
    return self.edad + other.edad # Retornar la suma de las edades

def __sub__(self, other): # Método sub / restar dos clases
    return self.edad - other.edad # Retornar la resta de las edades

def __mul__(self, other): # Método mul / multiplicar dos clases
    return self.edad * other.edad # Retornar la multiplicación de las edades

def __truediv__(self, other): # Método truediv / dividir dos clases
    return self.edad / other.edad # Retornar la división de las edades

def __pow__(self, other): # Método pow / elevar una clase a otra clase
    return self.edad ** other.edad # Retornar la potencia de las edades

def __eq__(self, other): # Método eq / comparar si dos clases son iguales
    return self.edad == other.edad # Retornar si las edades son iguales

def __ne__(self, other): # Método ne / comparar si dos clases son diferentes
    return self.edad != other.edad # Retornar si las edades son diferentes

def __lt__(self, other): # Método lt / comparar si una clase es menor que otra clase
    return self.edad < other.edad # Retornar si la edad es menor

def __le__(self, other): # Método le / comparar si una clase es menor o igual que otra clase
    return self.edad <= other.edad # Retornar si la edad es menor o igual

def __gt__(self, other): # Método gt / comparar si una clase es mayor que otra clase
    return self.edad > other.edad # Retornar si la edad es mayor

def __ge__(self, other): # Método ge / comparar si una clase es mayor o igual que otra clase   
    return self.edad >= other.edad # Retornar si la edad es mayor o igual

def __len__(self): # Método len / longitud de la clase / cantidad de elementos de la clase
    return self.edad # Retornar la edad

def __getitem__(self, key): # Método getitem / obtener un elemento de la clase
    return self.edad[key] # Retornar el elemento de la edad

def __setitem__(self, key, value): # Método setitem / establecer un elemento de la clase
    self.edad[key] = value # Establecer el elemento de la edad
    
def __delitem__(self, key): # Método delitem / eliminar un elemento de la clase
    del self.edad[key] # Eliminar el elemento de la edad
    
def __contains__(self, item): # Método contains / verificar si un elemento está en la clase
    return item in self.edad # Retornar si el elemento está en la edad

def __iter__(self): # Método iter / iterar la clase
    return iter(self.edad) # Retornar la iteración de la edad

def __next__(self): # Método next / siguiente elemento de la clase
    return next(self.edad) # Retornar el siguiente elemento de la edad

def __reversed__(self): # Método reversed / invertir la clase
    return reversed(self.edad) # Retornar la inversión de la edad


# Llamadas a funciones

print(suma(2, 3)) # Imprimir la suma de 2 y 3
print(resta(5, 3)) # Imprimir la resta de 5 y 3
print(multiplicacion(2, 3)) # Imprimir la multiplicación de 2 y 3  
print(division(6, 3)) # Imprimir la división de 6 y 3
print(potencia(2, 3)) # Imprimir la potencia de 2 elevado a 3
print(raiz(4)) # Imprimir la raíz cuadrada de 4
print(cuadrado(3)) # Imprimir el cuadrado de 3
print(cubo(2)) # Imprimir el cubo de 2
print(area_circulo(5)) # Imprimir el área de un círculo de radio 5
print(area_triangulo(3, 4)) # Imprimir el área de un triángulo de base 3 y altura 4
print(area_rectangulo(3, 4)) # Imprimir el área de un rectángulo de base 3 y altura 4
print(area_cuadrado(3)) # Imprimir el área de un cuadrado de lado 3
print(area_cubo(3)) # Imprimir el área de un cubo de lado 3
print(area_esfera(5)) # Imprimir el área de una esfera de radio 5
print(volumen_esfera(5)) # Imprimir el volumen de una esfera de radio 5
print(area_cilindro(5, 3)) # Imprimir el área de un cilindro de radio 5 y altura 3
print(volumen_cilindro(5, 3)) # Imprimir el volumen de un cilindro de radio 5 y altura 3
print(area_cono(5, 3)) # Imprimir el área de un cono de radio 5 y generatriz 3
print(volumen_cono(5, 3)) # Imprimir el volumen de un cono de radio 5 y altura 3
print(area_piramide(5, 3)) # Imprimir el área de una pirámide de base 5 y altura 3
print(volumen_piramide(5, 3)) # Imprimir el volumen de una pirámide de base 5 y altura 3
print(area_cuboide(5, 3, 4)) # Imprimir el área de un cuboide de largo 5, ancho 3 y profundidad 4
print(volumen_cuboide(5, 3, 4)) # Imprimir el volumen de un cuboide de largo 5, ancho 3 y profundidad 4
print(area_prisma(5, 3)) # Imprimir el área de un prisma de base 5 y altura 3
print(volumen_prisma(5, 3)) # Imprimir el volumen de un prisma de base 5 y altura 3


# Clases, métodos y objetos

class Persona: # Clase Persona
    def __init__(self, nombre, edad): # Método constructor / inicializar la clase
        self.nombre = nombre # Atributo nombre
        self.edad = edad # Atributo edad
        
    def saludar(self): # Método saludar / saludar a la persona
        return f"Hola, me llamo {self.nombre} y tengo {self.edad} años." # Retornar el saludo
    
class Estudiante(Persona): # Clase Estudiante / hereda de la clase Persona
    def __init__(self, nombre, edad, carrera): # Método constructor / inicializar la clase
        super().__init__(nombre, edad) # Inicializar la clase Persona
        self.carrera = carrera # Atributo carrera
        
    def estudiar(self): # Método estudiar / estudiar la carrera
        return f"Estoy estudiando {self.carrera}." # Retornar el mensaje
    
class Profesor(Persona): # Clase Profesor / hereda de la clase Persona
    def __init__(self, nombre, edad, especialidad): # Método constructor / inicializar la clase
        super().__init__(nombre, edad) # Inicializar la clase Persona
        self.especialidad = especialidad # Atributo especialidad
        
    def enseñar(self): # Método enseñar / enseñar la especialidad
        return f"Estoy enseñando {self.especialidad}." # Retornar el mensaje
    
persona = Persona("Juan", 30) # Objeto persona de la clase Persona se inicializa con nombre y edad 
estudiante = Estudiante("Ana", 25, "Ingeniería") # Objeto estudiante de la clase Estudiante se inicializa con nombre, edad y carrera
profesor = Profesor("Pedro", 35, "Matemáticas") # Objeto profesor de la clase Profesor se inicializa con nombre, edad y especialidad

print(persona.saludar()) # Imprimir el saludo de la persona


# Llamadas a métodos de clases

print(estudiante.saludar()) # Imprimir el saludo del estudiante
print(estudiante.estudiar()) # Imprimir el mensaje de estudiar del estudiante
print(profesor.saludar()) # Imprimir el saludo del profesor


# Llamadas a métodos de objetos

print(persona.saludar()) # Imprimir el saludo de la persona
print(estudiante.saludar()) # Imprimir el saludo del estudiante