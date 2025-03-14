"""
Resumen simplificado de lo esencial
"""

# Sintaxis Basica
# Python "indenta" los bloques de codigo
# Diferencia tambien mayusculas de minusculas

# Varible
# es un contenedor de elementos
# es un indentificador para ubicar elmentos guardado en la memoriasphinx-quickstart


# La variable siempre se declaran antes de ser utilizadas
# tambien deben ser iniciadas
int = 1
float = 1.1
string = "hola"
boolean = True # False

# aunque sean vacios hay que indicar valores
string = ""
int = 0
lista = []

# Operadores
# los hay de diferentes tipos:
# -- matematico --
# suma (+), resta (-), etc
# el signo + permite concatenar strings
saludo= "buenas" + " " + "tardes"
repeciticon = "hola " * 3 # "hola hola hola"

# -- comparativos --
# == (igual), != (diferente), > (Mayor), >= (mayor o igual), < (menos), <= (menor o igual)
# siempre devuelven valor booleano
# tambien podemos comparar strings
print("Hola" > "hola") # las mayus son mas pequeños que las minisculas = False

# -- asignacion --
# = (asignacion), += (suma y asigna), -= (resta y asigna)
int = 5
int = int + 5 # es lo mismo que int += 5
int += 5 # Optimiza un poco las variables
 
num_str = "5"
num_int = int(num_str) # casting -> convierte un string a un entero
num_5 = 5 # es un entero
num_5_str = str(num_5) # casting -> convierte un entero a un string
 
# Estructura de control
# hay de diferentes tipos
# -- condicionales --
 
# if condicion: -> ejecutara el codigo si la condicion es verdadera
# if conficion: / else: (para todo lo demas)
# if condicion: / elif condicion: 
# if condicion: / elif conficion: / else
 
# match variable:
#   case valor: -> si la variable tiene el valor indicado
#       se ejecuta el codigo siguiente
#   case _: -> equivale a "default" o un else
