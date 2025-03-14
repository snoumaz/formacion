'''
EJERCICIO 17: SEGUNDO NÚMERO MAYOR
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar el segundo número mayor.

Por ejemplo, si escribe:
2, 5, 3, 6, 9
La respuesta debe ser:
"El segundo número mayor es 6"
'''

try:
    numeros = list(set(int(x) for x in input("Introduce varios números separados por comas: ").split(",")))
    if len(numeros) < 2:
        print("Introduce al menos dos números diferentes.")
    else:
        numeros.sort(reverse=True)
        print(f"El segundo número mayor es {numeros[1]}")
except ValueError:
    print("Error, introduce solo números separados por comas")
