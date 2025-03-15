"""
LISTAS

Escriba un programa que permita crear una lista de palabras y que, a continuación, 
pida una palabra y diga cuántas veces aparece esa palabra en la lista.

Mediante este menú:

        LISTA DE PALABRAS

        Elige una opción:
        1. Crear lista, preguntando cuantas palabras incluirá
        2. Buscar palabra
        3. Añadir palabra a la lista
        4. Borrar palabra de la lista (si existe)
        5. Mostrar la lista de palabras

        Cualquier otra opción para salir

        Tu elección es ....

Requerimientos:

    -- Las opciones 2-3-4-5 deben verificar que existan elementos en la lista.
        Si no hay, mostrar el correspondiente mensaje.

    -- La opción 1 siempre crea una lista nueva. Por tanto elimina la
        lista anterior si existe.

    -- Cuando se pregunte cuantas palabras incluirá la lista, no hay que
        verificar que sea un número. Se asume que el usuario escribe un número.
        Lo que sí que se debe comprobar es que sea mayor a 0.

Posibles mejoras:

    -- Añadir una opción para editar una palabra en la lista.
    
    -- Añadir una opción para borrar todas las palabras de la lista.

    -- Comprobar que al pedir la cantidad de palbras de la lista, el usuario
        escribe un número entero.

    -- Y lo que se te ocurra...

  
"""

def mostrar_menu():
    print("\nLISTA DE PALABRAS")
    print("\nElige una opción:")
    print("1. Crear lista, preguntando cuántas palabras incluirá")
    print("2. Buscar palabra")
    print("3. Añadir palabra a la lista")
    print("4. Borrar palabra de la lista (si existe)")
    print("5. Mostrar la lista de palabras")
    print("6. Editar una palabra en la lista")
    print("7. Borrar todas las palabras de la lista")
    print("Cualquier otra opción para salir")

def crear_lista():
    global lista_palabras
    while True:
        try:
            cantidad = int(input("¿Cuántas palabras incluirá la lista?: "))
            if cantidad > 0:
                lista_palabras = [input(f"Palabra {i + 1}: ") for i in range(cantidad)]
                print("Lista creada con éxito.")
                break
            else:
                print("El número debe ser mayor a 0.")
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

def buscar_palabra():
    if not lista_palabras:
        print("La lista está vacía.")
        return
    palabra = input("Introduce la palabra a buscar: ")
    print(f"La palabra '{palabra}' aparece {lista_palabras.count(palabra)} veces en la lista.")

def añadir_palabra():
    if lista_palabras is None:
        print("Primero debes crear una lista.")
        return
    palabra = input("Introduce la palabra a añadir: ")
    lista_palabras.append(palabra)
    print(f"'{palabra}' añadida a la lista.")

def borrar_palabra():
    if not lista_palabras:
        print("La lista está vacía.")
        return
    palabra = input("Introduce la palabra a borrar: ")
    if palabra in lista_palabras:
        lista_palabras.remove(palabra)
        print(f"'{palabra}' eliminada de la lista.")
    else:
        print("La palabra no está en la lista.")

def mostrar_lista():
    if not lista_palabras:
        print("La lista está vacía.")
    else:
        print("Lista de palabras:", ", ".join(lista_palabras))

def editar_palabra():
    if not lista_palabras:
        print("La lista está vacía.")
        return
    palabra = input("Introduce la palabra a editar: ")
    if palabra in lista_palabras:
        nueva_palabra = input("Introduce la nueva palabra: ")
        lista_palabras[lista_palabras.index(palabra)] = nueva_palabra
        print("Palabra editada con éxito.")
    else:
        print("La palabra no está en la lista.")

def borrar_todas():
    global lista_palabras
    if not lista_palabras:
        print("La lista ya está vacía.")
    else:
        lista_palabras.clear()
        print("Todas las palabras han sido eliminadas.")

# Inicializar la lista de palabras
lista_palabras = []

# Bucle principal del menú
while True:
    mostrar_menu()
    opcion = input("Tu elección es: ")
    if opcion == "1":
        crear_lista()
    elif opcion == "2":
        buscar_palabra()
    elif opcion == "3":
        añadir_palabra()
    elif opcion == "4":
        borrar_palabra()
    elif opcion == "5":
        mostrar_lista()
    elif opcion == "6":
        editar_palabra()
    elif opcion == "7":
        borrar_todas()
    else:
        print("Saliendo del programa...")
        break
