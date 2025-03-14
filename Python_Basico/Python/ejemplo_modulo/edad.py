"""
Crea una funcion que la funcion se llamara calcula_edad
recibe 2 parametros.
fecha_nacimiento
fecha_actual

Ha de devolver la edad a partir de las 2 fechas

Parametros
fecha_nacimeinto str -> "dd-mm-aaaa"
fecha_actual str -> "dd-mm-aaaa"

Return
edad : int

Codigos de error:
-1 : dia o mes incorrecto
-2 : la fecha de nacimiento debe ser igual o menor de la actual

"""
# fecha_nacimiento = ("01-02-2010")
# fecha_actual = ("18-02-2025")

def calcula_edad(fecha_nacimiento:str,fecha_actual:str) -> int:
    """
    Crea una funcion que la funcion se llamara calcula_edad
    recibe 2 parametros.
    fecha_nacimiento
    fecha_actual

    Ha de devolver la edad a partir de las 2 fechas

    Parametros
    fecha_nacimeinto str -> "dd-mm-aaaa"
    fecha_actual str -> "dd-mm-aaaa"

    Return
    edad : int

    Codigos de error:
    -1 : dia o mes incorrecto
    -2 : la fecha de nacimiento debe ser igual o menor de la actual

"""
    #Convertir las fechas en str a valores numericos
    fecha_nacimiento = fecha_nacimiento.split("-")
    dia_n = int(fecha_nacimiento[0])
    mes_n = int(fecha_nacimiento[1])
    año_n = int(fecha_nacimiento[2])
    fecha_actual = fecha_actual.split("-")
    dia_a = int(fecha_actual[0])
    mes_a = int(fecha_actual[1])
    año_a = int(fecha_actual[2])

    # No Puede ser que un mes sea mayor a 12 o menor a 1
    # No puede ser que un dia menor a 1 o mayor a 31
    if (not 1<=mes_n<=12) or (not 1<=mes_a<=12) or (not 1<=dia_n<=31) or (not 1<=dia_a<=31):
        return -1
    # No se puede calcular la edad si la fecha de nacimiento
    # esposterior a la actual
    dif_año = año_a - año_n
    dif_meses = mes_a - mes_n
    dif_dias = dia_a - dia_n
    if (dif_año<0) or (dif_año==0 and dif_meses<0) or (dif_año==0 and dif_meses==0 and dif_dias<0):
        return -2

    # Calculo de la edad
    """
    Si la fecha de nacimiento en meses o en dias es menor a la actual es la resata de año_a - año_n -1
    Si la fecha de nacimiento de los meses es igual  i los dias es menor a la fecha - 1:
    Si la fecha de nacimiento de los meses y los dias son iguales o mayores restar año actual - año nacimiento
    
    """
    if (mes_n>mes_a and dia_n>dia_a) or (mes_n==mes_a and dia_n>dia_a):
        return dif_año -1
        #print(edad)
    else:
        return dif_año
        #print(edad)

#print(calcula_edad(fecha_nacimiento,fecha_actual))