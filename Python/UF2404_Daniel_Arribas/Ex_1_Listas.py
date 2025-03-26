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
# Funcion para crear una lista de palabras
def crear_lista(): # Funcion para crear una lista de palabras
    """Funcion para crear una lista de palabras"""
    try: # Se intenta ejecutar el siguiente código
        opcion_user= int(input("¿Cuantas palabras incluirá la lista?\n Ha de ser un número mayor a 0.\n")) # Pregunta al usuario cuantas palabras incluirá la lista
        if opcion_user > 0: # Si el número introducido es mayor a 0
            for palabra in range(opcion_user): # Se crea un bucle para introducir las palabras
                palabra = input("Introduce una palabra:\n").lower().capitalize() # Se pide al usuario que introduzca una palabra
                lista_palabras.append(palabra) # Se añade la palabra a la lista
            return f"Se ha creado la lista con la palabra {lista_palabras}." # Se devuelve la lista con las palabras introducidas
        else: # Si el número introducido no es mayor a 0
            return "El número introducido no es válido." # Se devuelve un mensaje de error
    except ValueError: # Si el usuario no introduce un número
        return "El valor introducido no es un número." # Se devuelve un mensaje de error

# Funcion para buscar una palabra en la lista
def buscar_palabra(): # Funcion para buscar una palabra en la lista
    """Funcion para buscar una palabra en la lista"""
    if not lista_palabras: # Si la lista está vacía
        return "La lista está vacía." # Se devuelve un mensaje de error
    palabra = input("Introduce la palabra que quieres buscar:\n").lower().capitalize() # Se pide al usuario que introduzca la palabra que quiere buscar
    if palabra in lista_palabras: # Si la palabra introducida está en la lista
        len(lista_palabras)
        return f"La palabra {palabra} está en la lista {len(lista_palabras)} veces."
    else: # Si la palabra introducida no está en la lista
        return f"La palabra {palabra} no está en la lista."

# Funcion para añadir una palabra a la lista
def añadir_palabra(): # Funcion para añadir una palabra a la lista
    """Funcion para añadir una palabra a la lista"""
    palabra = input("¿Que palabra quieres añadir a la lista?\n").lower().capitalize() # Se pide al usuario que introduzca la palabra que quiere añadirla a la lista
    lista_palabras.append(palabra) # Se añade la palabra a la lista
    return f"La palabra {palabra} ha sido añadida a la lista." # Se devuelve un mensaje de confirmación

# Funcion para borrar una palabra de la lista
def borrar_palabra(): # Funcion para borrar una palabra de la lista
    """Funcion para borrar una palabra de la lista"""
    if not lista_palabras: # Si la lista está vacía
        return "La lista está vacía." # Se devuelve un mensaje de error
    palabra = input("¿Que palabra quieres borrar de la lista?\n").lower().capitalize() # Se pide al usuario que introduzca la palabra que quiere borrar de la lista
    if palabra in lista_palabras: # Si la palabra está en la lista
        while palabra in lista_palabras: # Mientras la palabra esté en la lista
            lista_palabras.remove(palabra) # Se elimina la palabra de la lista
        return f"La palabra {palabra} ha sido eliminada de la lista." # Se devuelve un mensaje de confirmación
    else: # Si la palabra no está en la lista
        return f"La palabra {palabra} no está en la lista." # Se devuelve un mensaje de error

# Funcion para mostrar la lista de palabras
def mostrar_lista(): # Funcion para mostrar la lista de palabras
    """Funcion para mostrar la lista de palabras"""
    return f"La lista de palabras es {lista_palabras}." # Se devuelve la lista de palabras

lista_palabras = [] # Se crea una lista vacía

# Bucle para mostrar el menú
while True:
    menu = """
    
    LISTA DE PALABRAS

        Elige una opción:\n
        \t1. Crear lista\n
        \t2. Buscar palabra\n
        \t3. Añadir palabra a la lista\n
        \t4. Borrar palabra de la lista\n
        \t5. Mostrar la lista de palabras\n

        Cualquier otra opción para salir
    """
    print(menu)
    opcion_user = input("Que opcion eliges ==> ").strip()
    
    if opcion_user == "1":
         print(crear_lista())
         pass
    elif opcion_user == "2":
        print(buscar_palabra())
        pass
    elif opcion_user == "3":
        print(añadir_palabra())
        pass
    elif opcion_user == "4":
        print(borrar_palabra())
        pass
    elif opcion_user == "5":
        print(mostrar_lista())
        pass
    else:
        print("Saliendo del programa.")
        break
