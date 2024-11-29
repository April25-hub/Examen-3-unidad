print("April Arzaba Diaz")
print("1173")
print("3W")
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        """
        muestra los datos de la persona.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    
    def es_mayor_de_edad(self):
        """
        verifica si la persona es mayor de edad.
        """
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")

#esta linea dara un ejemplo de uso:
persona = Persona("April Arzaba Diaz", 17)
persona.mostrar_datos()
persona.es_mayor_de_edad()
