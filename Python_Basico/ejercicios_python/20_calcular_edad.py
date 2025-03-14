'''
EJERCICIO 20: CALCULAR EDAD
Haz un programa que pida al usuario su fecha de nacimiento y la fecha actual.
El programa debe mostrar la edad del usuario.
"Tienes XX años"

Nota: Hay que verificar año, mes y día para obtener la edad real.
No vale sólo el año.
Si alguien nació el 6/2/2000 y hoy es 7/2/2025 tiene 25 años
'''
import datetime

def obtener_fecha_nacimiento():
    while True:
        try:
            fecha_nacimiento = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
            dia, mes, año = map(int, fecha_nacimiento.split('/'))
            if datetime.date(año, mes, dia) <= datetime.date.today():
                return datetime.date(año, mes, dia)
            else:
                print("La fecha de nacimiento no puede ser en el futuro.")
        except ValueError:
            print("Formato de fecha incorrecto. Debe ser dd/mm/aaaa.")
            
        return None

def obtener_fecha_actual():
    return datetime.date.today()

def calcular_edad(fecha_nacimiento, fecha_actual):
    return fecha_actual.year - fecha_nacimiento.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))

# Ejecución del programa
fecha_nacimiento = obtener_fecha_nacimiento()
fecha_actual = obtener_fecha_actual()
edad = calcular_edad(fecha_nacimiento, fecha_actual)
print(f"Tienes {edad} años")
