'''
EJERCICIO 12: SUMA DEL USUARIO
En una sola instrucción (de una vez) pide al usuario
que introduzca varios números (fíjate en el ejemplo).
La respuesta del programa será la suma de todos ellos.
Puede escribir cualquier cantidad de números.

Por ejemplo, si escribe
2, 5, 3
La respuesta debe ser:
"El resultado de la suma es 10" 
'''
try:
    numeros = input("Introduce varios números separados por comas: \n")
    suma = sum([float(i) for i in numeros.split(",")]) # sumar los números introducidos independientemente de la cantidad de ellos y mostrar el resultado
    print(f"El resultado de la suma es {suma}")
except ValueError:
    print("Ha de ser numerico")