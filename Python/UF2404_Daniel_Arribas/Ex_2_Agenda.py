"""
AGENDA

Escribir un programa que implemente una agenda.
Supondremos que siempre se indicarán nombres diferentes.

En la agenda se podrán guardar nombres y números de teléfono. 
El programa nos dará el siguiente menú:

* Añadir/modificar: Nos pide un nombre. 
    -- Si el nombre se encuentra en la agenda, debe mostrar el teléfono y, 
    opcionalmente, permitir modificarlo si no es correcto, preguntando
    al usuario si quiere hacerlo. 
    -- Si el nombre no se encuentra debe añadirlo y también el teléfono correspondiente.

* Buscar: Nos pide una cadena de caracteres, 
    y nos muestras todos los contactos 
    cuyos nombres comiencen por dicha cadena.
    Por ejemplo, podemos tener contactos llamados "Mario", María", "Maria", "Mar",
    "Marta". Si buscamos "Mar" nos mostrará todos ellos. 
    Si no hay ningún contacto que comience por dicha cadena, 
    muestra el correspondiente mensaje de aviso:
    "No hay contactos que comiencen por la cadena introducida."

* Borrar: Nos pide un nombre completo y si existe nos preguntará si queremos borrarlo de la agenda. 
    Si no existe muestra el correspondiente mensaje de aviso.

* Listar: Nos muestra todos los contactos de la agenda.
    Si no hay ningún contacto, muestra el correspondiente mensaje de aviso.

* Salir, con un saludo final

Implementar el programa con un diccionario.
Como elemento de selección en el menú puedes usar letras, números o palabras completas
    (por ejemplo, "Añadir", "1", "A"), o incluso emojis.



Posibles mejoras:

* Implementar una opción en el menú que permita buscar un contacto por número de teléfono.

* Implementar el código como una función.

* Y lo que se te ocurra...

"""

agenda = {} # Se crea un diccionario vacío

# Funcion para añadir o modificar un contacto
def añadir_modificar():
    """Funcion para añadir y/o modificar un contacto"""
    nombre = input("Introduce el nombre del contacto:\n").lower().capitalize().strip() # Se pide al usuario que introduzca el nombre del contacto,
    # los datos se ponen en minusculas, se quitan los especios en blanco de delante y detras y se pone en mayusculas la primera letra.
    if nombre in agenda: # Si el nombre del contacto está en la agenda
        print(f"El telefono de {nombre} es {agenda[nombre]}.\n") # Se muestra el teléfono del contacto
        modifcar = input("¿Quieres modificar el contacto?\n").lower() # Se pregunta al usuario si quiere modificar el contacto
        try:
            if modifcar == "si":
                telefono = int(input("Introduce el nuevo teléfono del contacto:\n"))
                agenda[nombre] = telefono # Se modifica el teléfono del contacto
                return f"El contacto de {nombre} ha sido modificado con el numero {telefono}." # Se devuelve un mensaje de confirmación
            else:
                return "El contacto no ha sido modificado." # Se devuelve un mensaje de confirmación
        except ValueError:
            return "El valor que has introducio no es un numero."
    else: # Si el nombre del contacto no está en la agenda
        try:
            telefono = int(input(f"Introduce el telefono para {nombre}:\n")) # Se pide al usuario que introduzca el teléfono del contacto
            agenda[nombre] = telefono # Se añade el contacto a la agenda
            return f"Se ha añadido el contacto de {nombre} a la agenda correctamente." # Se devuelve un mensaje de confirmación
        except ValueError:
            return "El valor que has introducio no es un numero."
        
# Funcion para buscar un contacto
def buscar():
    """Funcion para buscar un contacto"""
    cadena = input("Introduce la cadena de caracteres para buscar el contacto:\n").lower().capitalize().strip() # Se pide al usuario que introduzca la cadena de caracteres
    # los datos se ponen en minusculas, se quitan los especios en blanco de delante y detras y se pone en mayusculas la primera letra.
    resultados = [nombre for nombre in agenda if nombre.startswith(cadena)] # Se buscan los contactos que comiencen con la cadena de caracteres
    if resultados: # Si hay resultados
        print(f"Contactos encontrados: {', '.join(resultados)}")
        eleccion = input("¿Desea modificar alguno de estos contactos? Si/No:\n").lower().strip() # Se pregunta al usuario si quiere modificar alguno de los contactos,
        # los datos se ponen en minusculas, se quitan los especios en blanco de delante y detras.
        if eleccion == "si":
            nombre = input("Introduce el nombre del contacto que desea modificar:\n").lower().capitalize().strip() # Se pide al usuario que introduzca el nombre del contacto que quiere modificar,
            # los datos se ponen en minusculas, se quitan los especios en blanco de delante y detras y se pone en mayusculas la primera letra.
            if nombre in resultados:
                try:
                    telefono = int(input(f"Introduce el nuevo teléfono para {nombre}:\n"))
                    agenda[nombre] = telefono
                    return f"El contacto de {nombre} ha sido modificado con el numero {telefono}."
                except ValueError:
                    return "El valor que has introducido no es válido."
            else:
                return "El contacto no está en la lista de resultados."
        else:
            return "No se ha modificado ningún contacto."
    else: # Si no hay resultados
        print("No hay contactos que comiencen por la cadena introducida.\n¿Quiere crear un nuevo contacto?")
        nuevo = input("Si/No:\n").lower().strip() # Se pregunta al usuario si quiere añadir un nuevo contacto
        # los datos se ponen en minusculas, se quitan los especios en blanco de delante y detras y se pone en mayusculas la primera letra.
        if nuevo == "si":
            try:
                telefono = int(input(f"Introduce el telefono para {cadena}:\n")) # Se pide al usuario que introduzca el teléfono del contacto
                agenda[cadena] = telefono # Se añade el contacto a la agenda
                return f"Se ha añadido el contacto de {cadena} a la agenda correctamente." # Se devuelve un mensaje de confirmación
            except ValueError: # Si el usuario no introduce un número
                return "El valor que has introducido no es válido."
        else:
            return "No se ha añadido el contacto a la agenda."
  

# Funcion para borrar un contacto
def borrar():
    """Funcion para borrar un contacto"""
    nombre = input("Introduce el nombre del contacto que desea eliminar:\n").lower().capitalize().strip() # Se pide al usuario que introduzca el nombre del contacto que quiere eliminar
    # los datos se ponen en minusculas, se quitan los especios en blanco de delante y detras y se pone en mayusculas la primera letra.
    if nombre not in agenda:
        return "El contacto no está en la agenda."
    else:
        try:
            borrar = input("¿Esta seguro de la eliminación del contacto?\n").lower().strip() # Se pregunta al usuario si está seguro de eliminar el contacto
            # los datos se ponen en minusculas, se quitan los especios en blanco de delante y detras y se pone en mayusculas la primera letra.
            if borrar == "si":
                agenda.pop(nombre) # Se elimina el contacto de la agenda
                return f"El contacto de {nombre} ha sido eliminado de la agenda."
            else:
                return "El contacto no ha sido eliminado."
        except ValueError:
            return "El valor que has introducio no es valido."


# Funcion para mostrar la agenda
def mostrar_agenda():
    """Funcion para mostrar Agenda"""
    if not agenda: # Si la agenda esta vacia 
        return "La agenda está vacía."
    else: # Si la agenda no está vacía
        agenda_str = "\n".join([f"{nombre}: {telefono}" for nombre, telefono in agenda.items()])
        return f"La agenda de Ferran:\n{agenda_str}" # Se devuelve la agenda formateada
    

# Bucle para mostrar el menú
while True:
    menu = """
    
    Agenda de contactos de Ferran

        Opciones disponibles:\n
        \t1. Añadir contacto o modificar\n
        \t2. Buscar contacto\n
        \t3. Borrar contacto\n
        \t4. Mostrar Agenda\n
        
        Cualquier otra opción para salir de la agenda
    """
    print(menu)
    opcion_user = input("¿Cual es su elección? ").strip()
    
    if opcion_user == "1":
         print(añadir_modificar())
         pass
    elif opcion_user == "2":
        print(buscar())
        pass
    elif opcion_user == "3":
        print(borrar())
        pass
    elif opcion_user == "4":
        print(mostrar_agenda())
        pass
    else:
        print("Saliendo de la agenda.")
        break




