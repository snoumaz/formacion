"""
TUPLAS
Son como listas pero inmutables de Datos
"""
mi_tupla = (3,4,5) # tambien se puede realizar sin parentesis ==> tupla
print(type(mi_tupla))

tupla = ("Anna", "Pou", 20, "anna@gmail.com") #
print(tupla)
# tupla[0] = "Marta" # No se puede modificar
# print(tupla)

# Como cambiar las tuplas hay que generar una lista temporal
lista_temporal = list(tupla)
print(lista_temporal)
lista_temporal[0] = "Marte"
print(lista_temporal)
tupla = tuple(lista_temporal) # vuelve a tupla la lista temporal
print(tupla[1:3]) # muestra los valores en la posicion 1 y 3

for item in tupla:
    print(item)
