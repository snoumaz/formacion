'''
EJERCICIO 6: CONVERSIÓN A GRADOS CELSIUS
Haz un programa que pida al usuario la temperatura en grados Fahrenheit
La respuesta del programa será:
"X grados Fahrenheit equivalen a Y grados Celsius" (los valores que sean)
Formúla de conversión : Fahrenheit = (Celsius * 9/5) + 32
'''

try:
    conversion = 32
    temperatura = float(input("Introduce una temperatura en grados Fahrenheit: \n")) # solicitar la temperatura en grados Fahrenheit
    resultado = (temperatura - conversion) * 5/9 # convertir la temperatura a grados Celsius
    print(f"{temperatura} grados Fahrenheit equivalen a {resultado} grados Celsius") # mostrar el resultado
except ValueError:
    print("Ha de ser numerico")