# Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__. Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.

class Calculadora():
    
    def __init__(self, numero1, numero2):
        self.num1 = int(input("Ingrese un numero: "))
        self.num2 = int(input("Ingrese otro numero: "))

    def suma(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "No se puede dividir por 0"


calcu = Calculadora(5,0)

print('Suma =', calcu.suma())
print('Resta =', calcu.restar())
print('Multiplicacion =', calcu.multiplicar())
print('Division = ', calcu.dividir())



