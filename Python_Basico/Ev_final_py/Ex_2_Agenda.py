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

def mostrar_menu():
    print("\nAGENDA")
    print("\nElige una opción:")
    print("1. Añadir/Modificar contacto")
    print("2. Buscar contacto por nombre")
    print("3. Buscar contacto por número")
    print("4. Borrar contacto")
    print("5. Listar todos los contactos")
    print("6. Salir")

def añadir_modificar_contacto():
    nombre = input("Introduce el nombre: ")
    if nombre in agenda:
        print(f"El número actual de {nombre} es {agenda[nombre]}")
        modificar = input("¿Quieres modificarlo? (s/n): ").strip().lower()
        if modificar == 's':
            agenda[nombre] = input("Introduce el nuevo número: ")
            print("Número actualizado.")
    else:
        numero = input("Introduce el número: ")
        agenda[nombre] = numero
        print("Contacto añadido.")

def buscar_contacto():
    cadena = input("Introduce una cadena para buscar: ")
    encontrados = {nombre: numero for nombre, numero in agenda.items() if nombre.startswith(cadena)}
    if encontrados:
        for nombre, numero in encontrados.items():
            print(f"{nombre}: {numero}")
    else:
        print("No hay contactos que comiencen por la cadena introducida.")

def buscar_por_numero():
    numero = input("Introduce el número a buscar: ")
    encontrados = [nombre for nombre, num in agenda.items() if num == numero]
    if encontrados:
        print(f"El número pertenece a: {', '.join(encontrados)}")
    else:
        print("No hay contactos con ese número.")

def borrar_contacto():
    nombre = input("Introduce el nombre a borrar: ")
    if nombre in agenda:
        confirmar = input(f"¿Seguro que deseas borrar a {nombre}? (s/n): ").strip().lower()
        if confirmar == 's':
            del agenda[nombre]
            print("Contacto eliminado.")
    else:
        print("El contacto no existe en la agenda.")

def listar_contactos():
    if not agenda:
        print("La agenda está vacía.")
    else:
        for nombre, numero in agenda.items():
            print(f"{nombre}: {numero}")

def ejecutar_agenda():
    while True:
        mostrar_menu()
        opcion = input("Tu elección es: ")
        if opcion == "1":
            añadir_modificar_contacto()
        elif opcion == "2":
            buscar_contacto()
        elif opcion == "3":
            buscar_por_numero()
        elif opcion == "4":
            borrar_contacto()
        elif opcion == "5":
            listar_contactos()
        elif opcion == "6":
            print("Saliendo de la agenda. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

# Inicializar la agenda como diccionario
agenda = {}

# Ejecutar la agenda
ejecutar_agenda()
6