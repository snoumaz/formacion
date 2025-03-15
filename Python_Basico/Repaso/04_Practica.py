"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. 
Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
Finalmente Llamar a la clase Calculadora.

    """
    
class Calculadora():
    def __init__(self):
        self.num1 = int(input("Ingrese el primer número: "))
        self.num2 = int(input("Ingrese el segundo número: "))
    
    def suma(self):
        return self.num1 + self.num2
    
    def resta(self):
        return self.num1 - self.num2
    
    def multiplicacion(self):
        return self.num1 * self.num2
    
    def division(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: División por cero"

# Crear una instancia de la clase Calculadora y llamar a sus métodos
calc = Calculadora()
print("Suma:", calc.suma())
print("Resta:", calc.resta())
print("Multiplicación:", calc.multiplicacion())
print("División:", calc.division())






