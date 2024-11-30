print("April Arzaba Diaz")
print("1173")
print("3W")
class Calculadora:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

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
            return "Error: Division por cero"

    def mostrar_resultados(self):
        print(f"suma: {self.suma()}")
        print(f"resta: {self.resta()}")
        print(f"multiplicacion: {self.multiplicacion()}")
        print(f"division: {self.division()}")

#esta linea dara un ejemplo de uso:
calc = Calculadora(10, 2)
calc.mostrar_resultados()
