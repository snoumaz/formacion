"""
DICCIONARIOS
EL acceso al dato se produce mediante un identificador
llamado "CLAVE". Se muestra de la siguiente manera:
"Clave" : "Valor"
Los diccionaros son mutables
Las claves pueden ser de diferentes tipos como:
string, int, float, tupla ...
{} <-- llaves
"""

dic_1 = {} # diccionario vacio tiene un valor booleano, si esta vacio es false
lista_vacia = [] # lista vacia tiene un valor booleano, si esta vacio es false

if not lista_vacia: # si la sita 
    print("La lista esta vacia")

dic_1 = {"nombre":"Maria","apellido":"UnPajote","edad":30}
print(dic_1["nombre"])
argumento = "direccion"
print(dic_1.get(argumento,f"Este {argumento} no exite en el diccionario")) # none es un booleano como 0 .get = un busca i compara

# Iteracion directa
for propiedad in dic_1: # nos da las "claves/argumentos "
    print(propiedad)

# Iteracion especifica
for propiedades in dic_1.keys():
    print(propiedades)

# Iteracion especifica valores
for propiedades in dic_1.values():
    print(propiedades)

for clave, valor in dic_1.items():
    print(f"{clave} : {valor}")

# Para añadir otro elemento o valor
# Para añadir un par de clave-valor
dic_1["pais"] = "Grecia"
# Para añadir o acer un update 
dic_update = {"ciudad":"Paris","edad":34}
dic_1.update(dic_update)
print(dic_1)

