from colorama import init, Fore, Style

# Inicializa colorama para que los colores funcionen en la terminal
init(autoreset=True)

# Se crea un diccionario vacío para almacenar los contactos
agenda = {}

# Funcion para validar el número de teléfono
def validar_telefono(telefono):
    """Funcion para validar el número de teléfono"""
    # Verifica que el teléfono no tenga más de 12 dígitos y que solo contenga números
    if len(telefono) > 12 or not telefono.isdigit():
        return False
    return True

# Funcion para añadir o modificar un contacto
def añadir_modificar():
    """Funcion para añadir y/o modificar un contacto"""
    # Solicita el nombre del contacto al usuario
    nombre = input("📇 Introduce el nombre del contacto:\n").lower().capitalize().strip()
    # Verifica si el contacto ya existe en la agenda
    if nombre in agenda:
        # Muestra el teléfono actual del contacto
        print(f"📞 El telefono de {nombre} es {agenda[nombre]}.\n")
        # Pregunta si se desea modificar el contacto
        modificar = input("✏️ ¿Quieres modificar el contacto? (si/no)\n").lower().strip()
        if modificar == "si":
            # Solicita el nuevo teléfono del contacto
            telefono = input("📞 Introduce el nuevo teléfono del contacto (máximo 12 dígitos):\n").strip()
            # Valida el nuevo teléfono
            if not validar_telefono(telefono):
                return "❌ El teléfono debe tener un máximo de 12 dígitos y solo contener números."
            # Actualiza el teléfono del contacto en la agenda
            agenda[nombre] = telefono
            return f"✅ El contacto de {nombre} ha sido modificado con el numero {telefono}."
        else:
            return "❌ El contacto no ha sido modificado."
    else:
        # Solicita el teléfono para el nuevo contacto
        telefono = input(f"📞 Introduce el telefono para {nombre} (máximo 12 dígitos):\n").strip()
        # Valida el teléfono
        if not validar_telefono(telefono):
            return "❌ El teléfono debe tener un máximo de 12 dígitos y solo contener números."
        # Añade el nuevo contacto a la agenda
        agenda[nombre] = telefono
        return f"✅ Se ha añadido el contacto de {nombre} a la agenda correctamente."

# Funcion para buscar un contacto
def buscar():
    """Funcion para buscar un contacto"""
    # Solicita la cadena de caracteres para buscar el contacto
    cadena = input("🔍 Introduce la cadena de caracteres para buscar el contacto:\n").lower().capitalize().strip()
    # Busca contactos que comiencen con la cadena introducida
    resultados = [nombre for nombre in agenda if nombre.startswith(cadena)]
    if resultados:
        # Muestra los contactos encontrados
        print(f"📇 Contactos encontrados: {', '.join(resultados)}")
        # Pregunta si se desea modificar alguno de los contactos encontrados
        eleccion = input("✏️ ¿Desea modificar alguno de estos contactos? (si/no):\n").lower().strip()
        if eleccion == "si":
            # Solicita el nombre del contacto que se desea modificar
            nombre = input("📇 Introduce el nombre del contacto que desea modificar:\n").lower().capitalize().strip()
            if nombre in resultados:
                # Solicita el nuevo teléfono para el contacto
                telefono = input(f"📞 Introduce el nuevo teléfono para {nombre} (máximo 12 dígitos):\n").strip()
                # Valida el nuevo teléfono
                if not validar_telefono(telefono):
                    return "❌ El teléfono debe tener un máximo de 12 dígitos y solo contener números."
                # Actualiza el teléfono del contacto en la agenda
                agenda[nombre] = telefono
                return f"✅ El contacto de {nombre} ha sido modificado con el numero {telefono}."
            else:
                return "❌ El contacto no está en la lista de resultados."
        else:
            return "❌ No se ha modificado ningún contacto."
    else:
        # Informa que no se encontraron contactos y pregunta si se desea crear un nuevo contacto
        print("❌ No hay contactos que comiencen por la cadena introducida.\n¿Quiere crear un nuevo contacto?")
        nuevo = input("✏️ Si/No:\n").lower().strip()
        if nuevo == "si":
            # Solicita el teléfono para el nuevo contacto
            telefono = input(f"📞 Introduce el telefono para {cadena} (máximo 12 dígitos):\n").strip()
            # Valida el teléfono
            if not validar_telefono(telefono):
                return "❌ El teléfono debe tener un máximo de 12 dígitos y solo contener números."
            # Añade el nuevo contacto a la agenda
            agenda[cadena] = telefono
            return f"✅ Se ha añadido el contacto de {cadena} a la agenda correctamente."
        else:
            return "❌ No se ha añadido el contacto a la agenda."

# Funcion para borrar un contacto
def borrar():
    """Funcion para borrar un contacto"""
    # Solicita el nombre del contacto que se desea eliminar
    nombre = input("🗑️ Introduce el nombre del contacto que desea eliminar:\n").lower().capitalize().strip()
    if nombre not in agenda:
        return "❌ El contacto no está en la agenda."
    else:
        # Pregunta si se está seguro de la eliminación del contacto
        borrar = input("🗑️ ¿Esta seguro de la eliminación del contacto? (si/no)\n").lower().strip()
        if borrar == "si":
            # Elimina el contacto de la agenda
            agenda.pop(nombre)
            return f"✅ El contacto de {nombre} ha sido eliminado de la agenda."
        else:
            return "❌ El contacto no ha sido eliminado."

# Funcion para mostrar la agenda
def mostrar_agenda():
    """Funcion para mostrar Agenda"""
    if not agenda:
        return "❌ La agenda está vacía."
    else:
        # Crea una cadena con todos los contactos y sus teléfonos
        agenda_str = "\n".join([f"{nombre}: {telefono}" for nombre, telefono in agenda.items()])
        return f"📇 La agenda de Ferran:\n{agenda_str}"

# Bucle para mostrar el menú
while True:
    # Muestra el menú de opciones
    menu = """
    📒 Agenda de contactos de Ferran

        Opciones disponibles:\n
        \t1. 📇 Añadir contacto o modificar\n
        \t2. 🔍 Buscar contacto\n
        \t3. 🗑️ Borrar contacto\n
        \t4. 📒 Mostrar Agenda\n
        
        Cualquier otra opción para salir de la agenda
    """
    print(menu)
    # Solicita la elección del usuario
    opcion_user = input("¿Cual es su elección? ").strip()
    
    if opcion_user == "1":
         print(añadir_modificar())
    elif opcion_user == "2":
        print(buscar())
    elif opcion_user == "3":
        print(borrar())
    elif opcion_user == "4":
        print(mostrar_agenda())
    else:
        print("👋 Saliendo de la agenda.")
        break




