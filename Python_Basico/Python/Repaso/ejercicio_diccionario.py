"""
Ejercicio Diccionario

Tenemos un sitio que registra los accesos de los usuarios.
Necesitamos un menu con estas opciones:
1. Añadir un Usuario 
    (si no exite)
2. Añadir una visita al usuario indicado 
    ( si el usuario no exite mostar error)
3. Mostrar las visitas del usuario que se decida
    (si el usuario no exite mostar error)
4. Mostrar las visitas de todos los usuarios
    (si no hay usuarios todavia indicarlo)
X. para Salir

Hay que hacerlo con un diccionaro
"""


# Limpiar la pantalla
import os
os.system("cls")

users = [] # Lista de usuarios vacía
while True: # Bucle infinito que si es verdad se ejecuta
    # variable que guarda el menú de opciones
    menu = """
1. Añadiremos un usuario 
2. Añadiremos una visita al usuario indicado 
3. Mostraremos las visitas del usuario que se decida
4. Mostraremos las visitas de todos los usuarios
X. Salir
"""
    print(menu) # Mostramos el menú en pantalla
    opcion = input("Elige tu opcion --> ").strip().lower() # variable que guarda la opción elegida por el usuario quitando los espacios y poniendo la primera letra en mayúscula

    match opcion: # Estructura de control match que evalua la variable opcion y ejecuta el código según el caso
        case "1": # Caso 1
            new_user = input("Nuevo usuario --> ").strip().title() # variable que guarda el nuevo usuario introducido por el usuario quitando los espacios y poniendo la primera letra en mayúscula
            if users: # Si la condición es verdadera para users se ejecuta el código
                user_in_list = [] # Lista vacía
                for user in users: # Para cada usuario en la lista de usuarios se ejecuta el código
                    user_in_list.append(user['nombre']) # Se añade el nombre del usuario a la lista user_in_list             
                if new_user not in user_in_list: # Si el nuevo usuario no está en la lista de usuarios se ejecuta el código
                    user_dic = {"nombre":new_user, "visitas": 0 } # La variable user_dic guarda un diccionario con el nombre del nuevo usuario y el número de visitas a 0
                    users.append(user_dic) # Se añade el diccionario a la lista de usuarios 
                    print(f"Usuario {new_user} añadido") # Se muestra en pantalla el mensaje
                else: # En caso contrario se ejecuta el código
                    print("El usuario ya existe") # Se muestra en pantalla el mensaje
            else: # En caso contrario se ejecuta el código y se añade el usuario a la lista de usuarios
                user_dic = {"nombre":new_user, "visitas": 0 } # La variable user_dic guarda un diccionario con el nombre del nuevo usuario y el número de visitas a 0
                users.append(user_dic) # Se añade el diccionario a la lista de usuarios
                print(f"Usuario {new_user} añadido")  # Se muestra en pantalla el mensaje
        case "2": # Caso 2
            if users: # Si la condición es verdadera para users se ejecuta el código
                nombre_usuario = input("Usuario --> ").strip().title() # variable que guarda el nombre del usuario introducido por el usuario quitando los espacios y poniendo la primera letra en mayúscula
                encontrado = False # Variable booleana que guarda el valor False
                for user in users: # Para cada usuario en la lista de usuarios se ejecuta el código
                    if user['nombre'] == nombre_usuario: # Si el nombre del usuario es igual al nombre del usuario introducido por el usuario se ejecuta el código
                        user['visitas'] += 1 # Se suma 1 al número de visitas del usuario
                        print(f"Visita añadida a {user['nombre']}") # Se muestra en pantalla el mensaje
                        encontrado = True # Se cambia el valor de la variable encontrado a True
                        break # Se rompe el bucle
                if not encontrado: # Si la variable encontrado es False se ejecuta el código
                    print("El usuario no existe") # Se muestra en pantalla el mensaje
            else: # En caso contrario se ejecuta el código
                print("No hay usuarios todavía") # Se muestra en pantalla el mensaje
        case "3": # Caso 3
            if users: # Si la condición es verdadera para users se ejecuta el código
                nombre_usuario = input("Usuario --> ").strip().title() # variable que guarda el nombre del usuario introducido por el usuario quitando los espacios y poniendo la primera letra en mayúscula
                encontrado = False # Variable booleana que guarda el valor False
                for user in users: # Para cada usuario en la lista de usuarios se ejecuta el código
                    if user['nombre'] == nombre_usuario: # Si el nombre del usuario es igual al nombre del usuario introducido por el usuario se ejecuta el código
                        print(f"El usuario {user['nombre']} ha visitado {user['visitas']} veces") # Se muestra en pantalla el mensaje
                        encontrado = True # Se cambia el valor de la variable encontrado a True
                        break # Se rompe el bucle
                if not encontrado: # Si la variable encontrado es False se ejecuta el código
                    print("El usuario no existe") # Se muestra en pantalla el mensaje
            else: # En caso contrario se ejecuta el código
                print("No hay usuarios todavía") # Se muestra en pantalla el mensaje
        case "4": # Caso 4
            if users: # Si la condición es verdadera para users se ejecuta el código, es decir si hay usuarios en la lista.
                print(users) # Se muestra en pantalla la lista de usuarios
            else: # En caso contrario se ejecuta el código
                print("No hay usuarios todavía") # Se muestra en pantalla el mensaje
        case "x": # Caso x para salir del programa 
            print("Fin del programa") # Se muestra en pantalla el mensaje
            break # Se rompe el bucle
        case _ : # Caso de no ser ninguna de las opciones anteriores
            print("Opción no reconocida.\nVuélvelo a probar.") # Se muestra en pantalla el mensaje
