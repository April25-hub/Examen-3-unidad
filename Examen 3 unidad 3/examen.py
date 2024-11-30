print("April Arzaba Diaz")
print("1173")
print("3W")
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def lado_mayor(self):
        """
        muestra el valor del lado mas grande.
        """
        return max(self.lado1, self.lado2, self.lado3)

    def tipo_triangulo(self):
        """
        determina el tipo de triangulo (equilatero, isosceles o escaleno).
        """
        if self.lado1 == self.lado2 == self.lado3:
            print("Triangulo equilatero.")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("triangulo isosceles.")
        else:
            print("triangulo escaleno.")
    
    def mostrar_datos(self):
        """
        muestra los datos del triangulo.
        """
        print(f"lados: {self.lado1}, {self.lado2}, {self.lado3}")
        print(f"lado mayor: {self.lado_mayor()}")
        self.tipo_triangulo()

#esta linea dara un ejemplo de uso:
triangulo = Triangulo(3, 4, 5)
triangulo.mostrar_datos()
