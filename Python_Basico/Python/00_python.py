"""
Mi primer programa con Python
Variables primitivas y funciones
"""

# Este es un comentario de una linea 
numero_entero = 2 # variable de numero int
numero_decimal = 4.5 # variable de numero float

saludo = "Buenas tardes" # variable string
# atajo de teclado para comentar seleccionar + control + ç
despedida = 'Adios'

declaration = "I'm a TI"
ejemplo_comilla_triple = """
    Estoy en una
    comilla triple
"""

# print(numero_entero)
# print(numero_decimal)
print(ejemplo_comilla_triple)

from datetime import datetime # importamos la clase datetime

print(datetime.now()) # imprime la fecha y hora actual

print("numero_entero es de tipo", type(numero_entero)) # averigua el tipo, pero no imprime en pantalla

# Booleanos son en mayusculas en minusculas son otra cosas
verdad = True
mentira = False

# Operaciones basicas son 7
suma = 1 + 7 # operacion suma
print(suma)

resta = 1 - 4 # operacion resta
print(resta)

multiplicacion = 4 * 2 # operacion multiplicacion
print(multiplicacion)

division = 10 / 3 # operacion division
print(division)

exponecial = 2 ** 3 # operacion exponente
print(exponecial)

exponecial = 50 ** 0.5 # raiz cuadrada
print(exponecial)

division_entera = 20 // 3 # operacion division entera (trunca la parte decimal)
print(division_entera)

modulo = 20 % 3 # operacion modulo (resto de la division entera)
print(modulo)

modulo = 9280129399 % 2 # operacion modulo (resto de la division entera)
print(modulo)

# Operaciones de prioridad por parentesis ( )
texto1 = "Hola"
texto2 = "Mundo"
texto_final = texto1 + " " + texto2
print(texto_final)

# Utilizando f-string
texto_final = f"{texto1} {texto2}"
print(texto_final)

# Utilizando la funcion format()
texto_final = "{} {}".format(texto1, texto2)
print(texto_final)

