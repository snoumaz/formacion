"""
Exercicis Python Bàsic 5/2/2025
"""

"""
# Ejercicio 1

# Un número primo es aquel que sólo es divisible por sí mismo o uno.

# Pediremos al usuario un número entero.
# Si escribe algo que no sea un número entero la aplicación debe responder: 
#     "Has de introducir un número entero".
# Daremos hasta tres oportunidades para que nos facilite un dato correcto.
# Pero si pasadas esas tres oportunidades sigue sin escribir un entero 
# la aplicación finalizará mostrando este mensaje:
#     "No has podido introducir un número entero en tres oportunidades
#     Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.
#     ".
# Si escribe un número entero puede pasar que
# -- sea un número primo; en ese caso la respuesta de la aplicación será:
#     "El número X es primo".
# -- no sea un número primo; en ese caso la respuesta de la aplicación será:
#     "El número X no es primo".

. 
"""

# Idea de como realizar el ejercicio

#for num in range(2, primo):
import os                                                           # <= Importamos la libreria OS
os.system("cls")                                                    # <= Solicitamos que realice primero el comando cls = limpiar la terminal

# Bucle que comprueba que el elemento introducido por el usuario es un numero entero y solo puede equivocarse 3 veces.
intentos = 0                                                        # <= Variable que guarda el numero de intentos
while intentos < 3:                                                 # <= Bucle que llega asta 3 intentos
    
    num = input("Dime un Numero entero: \n")                        # <= Variable que le pide al usuario que intorduzca un entero
    try:                                                            # <= comprueba
        num = int(num)                                              # <= transforma la variable num a entero
        break                                                       # <= si es entero cierra el bucle
    except ValueError:                                              # <= Por cada vez que el usuario introduce un valor no entero printa en pantalla un mensaje
        print("Has de introducir un numero entero") 
        intentos += 1                                               # <= Suma a intentos 1
        # print(intentos)                                           # <= Printar en pantalla el numero de intentos
    if intentos == 3:                                               # <= cuando el numero de intentos llega a 3 printa en pantalla el mensaje de error.
        print("""No has podido introducir un número entero en tres oportunidades
Puedes volverlo a intentar de nuevo ejecutando otra vez esta aplicación.""")
    
# Bucle que revisa que el numero facilitado por el usuario es primo o no.
es_primo = True                                                     # <- Crea variable es_primo dandole valor true
for primo in range(2, num):                                         # <- Crea un bucle que compara la variable primo en el rango desde 2 al a la variable num
    if num % primo == 0:                                            # <- Si el numero num es divisible por algun numero primo entre 2 y num-1 entonces es_primo es False
        es_primo = False                                            # <- Si es divisible por algun numero primo sale del bucle
        print(f"El número {num} no es primo")                       # <- Si es divisible por algun numero primo imprime el mensaje
        break      
if es_primo:                                                        # <- Si es_primo es True entonces imprime el mensaje
        print(f"El número {num} es primo")
 