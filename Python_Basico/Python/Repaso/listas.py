"""
Repaso Listas
las listas son colecciones mutables de datos
"""

# Lista vacia
lista = [] 
lista.append("Anna") # append es para añadir
print(lista)
lista[0] = "Marta"
print(lista)

# Las listas son conlecionnes de datos indexados
# eñ indice empieza en 0
lista[0]

lista_enteros = list(range(1,21,2))
print(lista_enteros)

lista_nombres = ["Pol","Noa","Sara","Pepe"]
# indice -->       0,    1,    2,     3
for nombre in lista_nombres:
    indice = lista_nombres.index(nombre)
    print(f"{indice}.{nombre}")

for indice, valor in enumerate(lista_nombres):
    print(f"{indice}.{valor}")

# Como copiar una lista

new_lista_1 = lista_nombres.copy()
new_lista_2 = lista_nombres[:]

# Mini ejercicio: obtener los numero elevados al cuadrado de una serie

lista_numeros = list(range(1,11))
# necesitamos una lista solo con los numeros elevados al cuadrado de la lista numeros
elevados = []
for indice, valor in enumerate(lista_numeros): # enumerate => enumerar el valor  que hay en la lista empezando en 0 ... infinito en este caso empieza en el 1
    elevados.append(valor ** 2)
print(elevados)

# RESOLUCIONES

# 1
lista_cuadrados = []
for numero in lista_numeros:
    lista_cuadrados.append(numero**2)
print(lista_cuadrados)

# 2
lista_cuadrados = print([num**2 for num in lista_numeros]) # me devuelves el cuadrado de la lista de numeros y muestra la lista


lista_ciudades = ["NY", "BCN", "LA"]
ny, bcn, la = lista_ciudades # asi se pueden generar variables de una tacada (no abusar, siempre hay que tener claro todo)
print(bcn)