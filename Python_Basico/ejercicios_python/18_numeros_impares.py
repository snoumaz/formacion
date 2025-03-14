'''
EJERCICIO 18: NÚMEROS IMPARES
Pídele al usuario que introduzca una serie de números,
comprendidos entre 1 y 20.
El programa debe mostrar los números impares introducidos
o un mensaje indicando que no hay ninguno.

Por ejemplo, si escribe:
2, 5, 3, 6, 9
La respuesta debe ser:
5, 3, 9
'''

try:
    nums = list(set(int(x) for x in input("Introduce varios números separados por comas: ").split(",")))
    impares = [num for num in nums if num%2 !=0]
    print(impares)
except ValueError:
    print("Han de ser Numeros.")