"""
Exercicis Python Bàsic 5/2/2025
"""

"""
Ejercicio 4
Mostraremos el mensaje: "Conversor de segundos"
A continuación pediremos al usuario una cantidad de segundos.

Le responderemos:
- Si son menos de 60 segundos, mostrará "X segundos son menos de 1 minuto"
- Si es igual o superior a 60 segundos le diremos:
    "X segundos son Y minutos y Z segundos"

Y así para las siguientes unidades de tiempo. Por tanto, si la cantidad de segundos 
supera la hora, le diremos cuantas horas, minutos y segundos son. 
Lo mismo si supera un día o una semana. 

. 
"""
import os
os.system("cls")

print("Conversor de segundos\n")

try: # Prueba y captura de errores
    segundos = int(input("Dime una cantidad de segundos a convertir: \n")) # Introduce una cantidad de segundos a convertir

    # Definición de unidades de tiempo en segundos
    segundos_minuto = 60                                                # variable segundos_minuto es igual a 60
    segundos_hora = segundos_minuto * 60                                # variable segundos_hora es igual a segundos_minuto por 60
    segundos_dia = segundos_hora * 24                                   # variable segundos_dia es igual a segundos_hora por 24
    segundos_semana = segundos_dia * 7                                  # variable segundos_semana es igual a segundos_dia por 7
    segundos_mes = segundos_dia * 30                                    # variable segundos_mes es igual a segundos_dia por 30.44
    segundos_año = segundos_dia * 365                                   # variable segundos_año es igual a segundos_dia por 365

    # Conversión de segundos a semanas, días, horas, minutos y segundos restantes
    años = segundos // segundos_año                                     # variable años es igual a segundos dividido por segundos_año
    segundos %= segundos_año                                            # variable segundos es igual a segundos modulo segundos_año

    meses = segundos // segundos_mes                                    # variable meses es igual a segundos dividido por segundos_mes
    segundos %= segundos_mes                                            # variable segundos es igual a segundos modulo segundos_mes

    semanas = segundos // segundos_semana                               # variable semanas es igual a segundos dividido por segundos_semana
    segundos %= segundos_semana                                         # variable segundos es igual a segundos modulo segundos_semana

    dias = segundos // segundos_dia                                     # variable dias es igual a segundos dividido por segundos_dia
    segundos %= segundos_dia                                            # variable segundos es igual a segundos modulo segundos_dia

    horas = segundos // segundos_hora                                   # variable horas es igual a segundos dividido por segundos_hora
    segundos %= segundos_hora                                           # variable segundos es igual a segundos modulo segundos_hora

    minutos = segundos // segundos_minuto                               # variable minutos es igual a segundos dividido por segundos_minuto
    segundos %= segundos_minuto                                         # variable segundos es igual a segundos modulo segundos_minuto

    # Construcción del mensaje de salida
    resultado = str(segundos) + " segundos son "                        # variable resultado es un string y es igual a segundos mas "segundos son"

    if años > 0: # condición si años es mayor que 0
        resultado += str(años) + " año" + ("s" if años > 1 else "") + ", " # resultado es igual a resultado mas años mas "año" si años es mayor que 1 si no es ""
    if meses > 0: # condición si meses es mayor que 0
        resultado += str(meses) + " mes" + ("es" if meses > 1 else "") + ", " # resultado es igual a resultado mas meses mas "mes" si meses es mayor que 1 si no es ""
    if semanas > 0: # condición si semanas es mayor que 0
        resultado += str(semanas) + " semana" + ("s" if semanas > 1 else "") + ", " # resultado es igual a resultado mas semanas mas "semana" si semanas es mayor que 1 si no es ""
    if dias > 0: # condición si dias es mayor que 0
        resultado += str(dias) + " día" + ("s" if dias > 1 else "") + ", " # resultado es igual a resultado mas dias mas "día" si dias es mayor que 1 si no es ""
    if horas > 0: # condición si horas es mayor que 0
        resultado += str(horas) + " hora" + ("s" if horas > 1 else "") + ", " # resultado es igual a resultado mas horas mas "hora" si horas es mayor que 1 si no es ""
    if minutos > 0: # condición si minutos es mayor que 0
        resultado += str(minutos) + " minuto" + ("s" if minutos > 1 else "") + " y " # resultado es igual a resultado mas minutos mas "minuto" si minutos es mayor que 1 si no es "" y

    resultado += str(segundos) + " segundo" + ("s" if segundos != 1 else "") # resultado es igual a resultado mas segundos mas "segundo" si segundos es diferente de 1 si no es ""

    print(resultado)                                                    # imprime resultado

except ValueError:
    print("Solo son válidos números.")
